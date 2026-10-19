"""
Research Data Analysis Toolkit for PhD Dissertation (Marketing & Business Administration)
Automated screening, Cronbach's Alpha, Harman's Single Factor Test (CMB), and Descriptive Statistics.
"""

import sys
import os
import argparse
import numpy as np
import pandas as pd


def compute_cronbach_alpha(df_items: pd.DataFrame) -> dict:
    """
    Computes Cronbach's Alpha and Item-Total Correlation for a set of items.
    """
    # Drop rows with NaN
    clean_df = df_items.dropna()
    k = clean_df.shape[1]
    n = clean_df.shape[0]

    if k < 2:
        return {"alpha": np.nan, "item_stats": {}}

    item_variances = clean_df.var(axis=0, ddof=1)
    total_scores = clean_df.sum(axis=1)
    total_variance = total_scores.var(ddof=1)

    if total_variance == 0:
        alpha = 0.0
    else:
        alpha = (k / (k - 1)) * (1 - (item_variances.sum() / total_variance))

    item_stats = {}
    for col in clean_df.columns:
        other_items = clean_df.drop(columns=[col])
        if other_items.shape[1] > 1:
            other_total = other_items.sum(axis=1)
            # Item-rest correlation
            if clean_df[col].std() > 0 and other_total.std() > 0:
                corr = clean_df[col].corr(other_total)
            else:
                corr = 0.0
            # Alpha if item deleted
            k_del = other_items.shape[1]
            var_del = other_items.var(axis=0, ddof=1).sum()
            tot_var_del = other_total.var(ddof=1)
            alpha_if_del = (k_del / (k_del - 1)) * (1 - (var_del / tot_var_del)) if tot_var_del > 0 else 0.0
        else:
            corr = np.nan
            alpha_if_del = np.nan

        item_stats[col] = {
            "mean": clean_df[col].mean(),
            "sd": clean_df[col].std(),
            "corrected_item_total_corr": corr,
            "alpha_if_deleted": alpha_if_del
        }

    return {
        "alpha": alpha,
        "sample_size": n,
        "item_count": k,
        "item_stats": item_stats
    }


def compute_descriptive_stats(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    """
    Computes Mean, SD, Skewness, Kurtosis for items.
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    subset = df[columns].dropna()
    results = []
    for col in columns:
        series = subset[col]
        mean = series.mean()
        sd = series.std()
        skew = series.skew()
        kurt = series.kurtosis()
        
        # Normality assessment (Kline 2016: |skew| <= 2, |kurt| <= 7)
        normal_kline = (abs(skew) <= 2.0) and (abs(kurt) <= 7.0)

        results.append({
            "Variable/Item": col,
            "N": len(series),
            "Mean": round(mean, 3),
            "Std Dev": round(sd, 3),
            "Skewness": round(skew, 3),
            "Kurtosis": round(kurt, 3),
            "Normality (Kline 2016)": "Acceptable" if normal_kline else "Caution"
        })

    return pd.DataFrame(results)


def harman_single_factor_test(df: pd.DataFrame, items: list = None) -> dict:
    """
    Performs Harman's Single Factor Test to assess Common Method Bias (CMB)
    using Principal Component Analysis (eigen-decomposition of correlation matrix).
    """
    if items is None:
        items = df.select_dtypes(include=[np.number]).columns.tolist()

    clean_data = df[items].dropna()
    if clean_data.shape[1] < 2:
        return {"error": "Need at least 2 items for PCA"}

    # Standardize data
    std_data = (clean_data - clean_data.mean()) / clean_data.std()
    
    # Correlation matrix
    corr_matrix = np.corrcoef(std_data, rowvar=False)
    
    # Eigenvalues
    eigenvalues, _ = np.linalg.eigh(corr_matrix)
    eigenvalues = np.sort(eigenvalues)[::-1]  # Sort descending
    
    total_variance = np.sum(eigenvalues)
    first_factor_var = eigenvalues[0]
    pct_variance_explained = (first_factor_var / total_variance) * 100.0

    cmb_risk = "High (Risk of Common Method Bias)" if pct_variance_explained >= 50.0 else "Low (No Serious CMB Detected)"

    return {
        "num_items": len(items),
        "sample_size": len(clean_data),
        "first_eigenvalue": round(first_factor_var, 3),
        "total_variance_pct": round(pct_variance_explained, 2),
        "threshold": "< 50% (Podsakoff et al., 2003)",
        "assessment": cmb_risk
    }


def main():
    parser = argparse.ArgumentParser(description="PhD Marketing & Business Data Analysis Toolkit")
    parser.add_argument("--file", type=str, required=True, help="Path to CSV or Excel dataset")
    parser.add_argument("--task", type=str, choices=["descriptive", "harman", "alpha", "all"], default="all")
    parser.add_argument("--items", type=str, default="", help="Comma-separated list of column names")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    # Load dataset
    if args.file.endswith(".xlsx") or args.file.endswith(".xls"):
        df = pd.read_excel(args.file)
    else:
        df = pd.read_csv(args.file)

    print(f"\n=======================================================")
    print(f"DATASET LOADED: {os.path.basename(args.file)}")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"=======================================================\n")

    selected_cols = [c.strip() for c in args.items.split(",") if c.strip()] if args.items else None

    if args.task in ["descriptive", "all"]:
        print("--- DESCRIPTIVE STATISTICS & NORMALITY TEST (KLINE 2016) ---")
        desc_df = compute_descriptive_stats(df, selected_cols)
        print(desc_df.to_string(index=False))
        print("\n")

    if args.task in ["harman", "all"]:
        print("--- HARMAN'S SINGLE FACTOR TEST (COMMON METHOD BIAS - CMB) ---")
        harman_res = harman_single_factor_test(df, selected_cols)
        for k, v in harman_res.items():
            print(f"  {k}: {v}")
        print("\n")

    if args.task in ["alpha", "all"]:
        if selected_cols:
            print(f"--- CRONBACH'S ALPHA TEST FOR: {', '.join(selected_cols)} ---")
            alpha_res = compute_cronbach_alpha(df[selected_cols])
            print(f"  Overall Cronbach's Alpha: {round(alpha_res['alpha'], 3)}")
            print(f"  Number of Items: {alpha_res['item_count']}")
            print(f"  Sample Size: {alpha_res['sample_size']}")
            print("\n  Item-Level Statistics:")
            item_df = pd.DataFrame.from_dict(alpha_res["item_stats"], orient="index")
            print(item_df.round(3).to_string())
            print("\n")
        else:
            print("Note: To run Cronbach's Alpha on specific constructs, provide --items item1,item2,item3")


if __name__ == "__main__":
    main()
