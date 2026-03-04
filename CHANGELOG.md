# Changelog

All notable changes to The American Standard repository will be documented here.

## [v1.0.0] - 2026-03-04

### Added
- Full static mirror of americanstandardshop.org for GitHub Pages hosting
- Python fetch script (`scripts/fetch_source.py`) for refreshing the static mirror
- Source configuration YAML (`sources/americanstandardshop.org.yaml`) with fetch metadata
- GitHub Pages redirect (`docs/index.html`) pointing to the site mirror
- WordPress REST API data snapshots (pages, product lines, OEmbed endpoints)
- SQL index troubleshooting documentation in README
- Releases view page (`docs/releases.html`)

### Details
- Site mirrors americanstandardshop.org, a TAA/BAA-compliant apparel shop
- Includes product line pages: Mens Cotton Polo, PT Uniform Set, Chef Wear
- Static assets from wp-content (Blocksy theme, Elementor page builder)
