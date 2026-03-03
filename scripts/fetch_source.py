#!/usr/bin/env python3
"""Fetch and store the HTML source for americanstandardshop.org."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch_html(url: str, timeout: int) -> str:
    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; source-bot/1.0)"},
    )
    with urlopen(request, timeout=timeout) as response:  # noqa: S310
        return response.read().decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download page source into source/americanstandardshop.org/index.html"
    )
    parser.add_argument(
        "--url",
        default="https://americanstandardshop.org/",
        help="URL to fetch (default: %(default)s)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds (default: %(default)s)",
    )
    args = parser.parse_args()

    output_path = Path("source/americanstandardshop.org/index.html")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        html = fetch_html(args.url, args.timeout)
    except HTTPError as exc:
        print(f"HTTP error while fetching {args.url}: {exc}")
        return 1
    except URLError as exc:
        print(f"Network error while fetching {args.url}: {exc}")
        return 1

    output_path.write_text(html, encoding="utf-8")
    print(f"Saved source to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
