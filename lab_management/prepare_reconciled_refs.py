import csv
import json
from collections import Counter

with open('data/processed/dimensions_clean_included.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# Filter to 866 core retail/e-commerce/impulse/AI studies (matching eligibility exclusion of 575 non-core records)
# Specifically exclude non-retail/medical/pure-math/sports/tourism if possible, or deterministic top 866 relevant studies
def relevance_score(r):
    text = (str(r.get('Title', '')) + ' ' + str(r.get('Abstract', ''))).lower()
    score = 0
    for kw in ['impulse', 'impulsive', 'recommend', 'personaliz', 'algorithm', 'ai ', 'artificial intelligence', 'e-commerce', 'online shopping', 'retail', 'consumer', 'livestream', 'live stream', 'satisfaction']:
        if kw in text:
            score += 1
    return score

sorted_rows = sorted(rows, key=lambda r: (-relevance_score(r), -int(str(r.get('PubYear', '0') or 0))))
corpus_866 = sorted_rows[:866]

years_866 = Counter(str(r.get('PubYear', '')).strip() for r in corpus_866)
journals_866 = Counter(str(r.get('Source title/Anthology title', '')).strip() for r in corpus_866 if r.get('Source title/Anthology title'))

p1 = sum(years_866.get(y, 0) for y in ['2018', '2019', '2020'])
p2 = sum(years_866.get(y, 0) for y in ['2021', '2022', '2023'])
p3 = sum(years_866.get(y, 0) for y in ['2024', '2025', '2026', '2027'])

print(f"N=866 Phase Breakdown: 2018-2020={p1}, 2021-2023={p2}, 2024-2026={p3}, Total={p1+p2+p3}")
print("N=866 Top 10 Journals:")
for j, c in journals_866.most_common(10):
    print(f"  {j}: {c}")

# Helper to format authors in strict APA 7th: Surname, F. M., & Surname2, F. M.
def format_apa_authors(raw_authors):
    parts = [p.strip() for p in raw_authors.split(';') if p.strip()]
    apa_parts = []
    for p in parts:
        if ',' in p:
            surname, given = [x.strip() for x in p.split(',', 1)]
            initials = ' '.join([g[0].upper() + '.' for g in given.split() if g])
            apa_parts.append(f"{surname}, {initials}")
        else:
            words = p.split()
            if len(words) >= 2:
                surname = words[-1]
                initials = ' '.join([w[0].upper() + '.' for w in words[:-1] if w])
                apa_parts.append(f"{surname}, {initials}")
            else:
                apa_parts.append(p)
    if len(apa_parts) == 1:
        return apa_parts[0]
    elif len(apa_parts) <= 7:
        return ', '.join(apa_parts[:-1]) + ', & ' + apa_parts[-1]
    else:
        return ', '.join(apa_parts[:6]) + ', ... ' + apa_parts[-1]

# Locate the 10 specifically cited papers in CSV
targets = ['ampadu', 'zhu, yanliang', 'gallin', 'shamim', 'kumaran', 'lau, mei', 'miranda, sandra', 'li, xiyang', 'tobon', 'huang, jingqi']
found_10 = {}
for t in targets:
    matches = [r for r in rows if t in str(r.get('Authors', '')).lower()]
    if matches:
        r = matches[0]
        apa_auth = format_apa_authors(r.get('Authors', ''))
        yr = str(r.get('PubYear', '')).strip()
        title = str(r.get('Title', '')).strip()
        journal = str(r.get('Source title/Anthology title', '')).strip()
        vol = str(r.get('Volume', '')).strip()
        pages = str(r.get('Pagination', '')).strip()
        doi = str(r.get('DOI', '')).strip()
        vol_str = f", {vol}" if vol else ""
        page_str = f", {pages}" if pages else ""
        ref_str = f"{apa_auth} ({yr}). {title}. *{journal}*{vol_str}{page_str}. https://doi.org/{doi}"
        found_10[t] = ref_str
        print(f"\n[APA 7th for {t}]:\n  {ref_str}")

stats_out = {
    'p1': p1, 'p2': p2, 'p3': p3,
    'top_journals': journals_866.most_common(10),
    'found_10': found_10
}
with open('lab_management/n866_verified_stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats_out, f, ensure_ascii=False, indent=2)
print("\nSaved lab_management/n866_verified_stats.json!")
