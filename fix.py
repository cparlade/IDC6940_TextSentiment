import re, pandas as pd, pathlib

RAW_TXT = pathlib.Path("data/raw/Sentences_AllAgree.txt")
out_csv = pathlib.Path("data/raw/phrasebank_sentences_allagree.csv")

rows = []
pat = re.compile(r'^\s*(positive|neutral|negative)\s*[@:\-\|]?\s*(.*)$', re.I)
for line in RAW_TXT.read_text(encoding="utf-8").splitlines():
    line=line.strip()
    if not line: continue
    m = pat.match(line)
    if m:
        label = m.group(1).lower()
        sent  = m.group(2).strip()
    else:
        # fallback: label at end like "… (positive)"
        m2 = re.search(r'\((positive|neutral|negative)\)\s*$', line, re.I)
        if not m2:
            continue
        label = m2.group(1).lower()
        sent  = re.sub(r'\s*\((positive|neutral|negative)\)\s*$', '', line, flags=re.I).strip()
    rows.append({"sentence": sent, "label_name": label})

df = pd.DataFrame(rows)
df.to_csv(out_csv, index=False)
print(df.shape, "→ wrote", out_csv)