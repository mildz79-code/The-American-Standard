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
