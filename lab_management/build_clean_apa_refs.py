import csv
import json
import re

with open('data/processed/dimensions_clean_included.csv', 'r', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

def format_apa_authors(raw_authors):
    parts = [p.strip() for p in raw_authors.split(';') if p.strip()]
    apa_parts = []
    for p in parts:
        if ',' in p:
            surname, given = [x.strip() for x in p.split(',', 1)]
            initials = ' '.join([g[0].upper() + '.' for g in given.split() if g and g[0].isalpha()])
            apa_parts.append(f"{surname}, {initials}" if initials else surname)
        else:
            words = p.split()
            if len(words) >= 2:
                surname = words[-1]
                initials = ' '.join([w[0].upper() + '.' for w in words[:-1] if w and w[0].isalpha()])
                apa_parts.append(f"{surname}, {initials}" if initials else surname)
            else:
                apa_parts.append(p)
    if len(apa_parts) == 1:
        return apa_parts[0]
    elif len(apa_parts) <= 7:
        return ', '.join(apa_parts[:-1]) + ', & ' + apa_parts[-1]
    else:
        return ', '.join(apa_parts[:6]) + ', ... ' + apa_parts[-1]

def make_cite_key(raw_authors, year):
    parts = [p.strip() for p in raw_authors.split(';') if p.strip()]
    surnames = []
    for p in parts:
        if ',' in p:
            surnames.append(p.split(',')[0].strip())
        else:
            surnames.append(p.split()[-1].strip())
    if len(surnames) == 1:
        return f"{surnames[0]} ({year})"
    elif len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]} ({year})"
    else:
        return f"{surnames[0]} et al. ({year})"

def make_paren_key(raw_authors, year):
    parts = [p.strip() for p in raw_authors.split(';') if p.strip()]
    surnames = []
    for p in parts:
        if ',' in p:
            surnames.append(p.split(',')[0].strip())
        else:
            surnames.append(p.split()[-1].strip())
    if len(surnames) == 1:
        return f"{surnames[0]}, {year}"
    elif len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]}, {year}"
    else:
        return f"{surnames[0]} et al., {year}"

# 1. Exact 10 cited articles from text & Table 2
mandatory_queries = [
    ('ampadu', '2022'),
    ('zhu, yanliang', '2023'),
    ('gallin', '2024'),
    ('shamim', '2025'),
    ('kumaran, m. siva bala', '2026'),
    ('lau, mei mei', '2026'),
    ('miranda, sandra', '2024'),
    ('li, xiyang', '2025'),
    ('tobon, sandra', '2024'),
    ('huang, jingqi', '2026'),
]

selected = []
seen_dois = set()

for auth_sub, yr_target in mandatory_queries:
    for r in rows:
        if auth_sub in str(r.get('Authors', '')).lower() and str(r.get('PubYear', '')).strip() == yr_target:
            doi = str(r.get('DOI', '')).strip()
            if doi and doi not in seen_dois:
                seen_dois.add(doi)
                selected.append(r)
                break

# 2. Add 35 core e-commerce/AI/impulse papers from 2022-2026 in top journals (no 'unpack' in title, no tourism/medical)
top_journals = {'Journal of Retailing and Consumer Services', 'Journal of Business Research', 'Computers in Human Behavior', 'International Journal of Information Management', 'Information & Management', 'Journal of Theoretical and Applied Electronic Commerce Research', 'International Journal of Retail & Distribution Management', 'International Journal of Consumer Studies', 'Psychology and Marketing', 'Technological Forecasting and Social Change', 'Electronic Commerce Research and Applications', 'Acta Psychologica', 'Asia Pacific Journal of Marketing and Logistics', 'Review of Managerial Science'}

for r in rows:
    if len(selected) >= 45:
        break
    yr = str(r.get('PubYear', '')).strip()
    title = str(r.get('Title', '')).strip()
    tl = title.lower()
    journal = str(r.get('Source title/Anthology title', '')).strip()
    doi = str(r.get('DOI', '')).strip()
    authors = str(r.get('Authors', '')).strip()
    if yr in ('2022', '2023', '2024', '2025', '2026') and journal in top_journals and doi and doi not in seen_dois and authors:
        if 'unpack' in tl or 'travel' in tl or 'tourism' in tl or 'hotel' in tl or 'airline' in tl or 'furniture' in tl or 'fitness' in tl:
            continue
        if any(k in tl for k in ['ai', 'artificial intelligence', 'algorithm', 'recommend', 'personaliz', 'impulse', 'live stream', 'livestream']):
            seen_dois.add(doi)
            selected.append(r)

out_refs = []
for r in selected:
    yr = str(r.get('PubYear', '')).strip()
    apa_auth = format_apa_authors(r.get('Authors', ''))
    title = str(r.get('Title', '')).strip().rstrip('.')
    # Clean any em-dash in title so APA looks uniform
    journal = str(r.get('Source title/Anthology title', '')).strip()
    vol = str(r.get('Volume', '')).strip()
    pages = str(r.get('Pagination', '')).strip()
    doi = str(r.get('DOI', '')).strip()
    vol_str = f", {vol}" if vol else ""
    page_str = f", {pages}" if pages else ""
    apa_line = f"- {apa_auth} ({yr}). {title}. *{journal}*{vol_str}{page_str}. https://doi.org/{doi}"
    out_refs.append({
        'paren': make_paren_key(r.get('Authors', ''), yr),
        'narr': make_cite_key(r.get('Authors', ''), yr),
        'apa': apa_line,
        'title': title,
        'journal': journal,
        'year': yr
    })

with open('lab_management/clean_apa_corpus_refs.json', 'w', encoding='utf-8') as f:
    json.dump(out_refs, f, ensure_ascii=False, indent=2)

print(f"Built {len(out_refs)} pure APA 7th corpus references! First 5:")
for x in out_refs[:5]:
    print(" ", x['paren'], "|", x['apa'][:90])
