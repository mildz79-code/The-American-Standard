# The-American-Standard Source

This repository contains a reusable web source definition for:

- `https://americanstandardshop.org/`

## Included

- `sources/americanstandardshop.org.yaml` — source configuration metadata.
- `scripts/fetch_source.py` — a small fetch utility that downloads the page HTML into `source/`.

## Usage

```bash
python3 scripts/fetch_source.py
```

By default this creates:

- `source/americanstandardshop.org/index.html`

You can optionally pass a custom URL:

```bash
python3 scripts/fetch_source.py --url https://americanstandardshop.org/
```

## SQL troubleshooting

If you hit an error like:

```text
ERROR: 42P07: relation "idx_wip_po_number" already exists
```

your migration/query is trying to create an index that is already present.
Use an idempotent statement instead:

```sql
CREATE INDEX IF NOT EXISTS idx_wip_po_number
  ON wip (po_number);
```

If the existing index has the wrong definition, recreate it safely:

```sql
DROP INDEX IF EXISTS idx_wip_po_number;
CREATE INDEX idx_wip_po_number ON wip (po_number);
```
