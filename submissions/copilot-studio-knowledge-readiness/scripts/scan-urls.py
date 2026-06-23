#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path
from urllib import request
from urllib.error import URLError


TIMEOUT_SECONDS = 15
USER_AGENT = "ckr-scan-urls/1.0 (+https://github.com/microsoft/cat-agent-skills)"


def extract_tag(html: str, tag_name: str) -> str:
    match = re.search(rf"<{tag_name}[^>]*>([\s\S]*?)</{tag_name}>", html, re.IGNORECASE)
    return clean(match.group(1)) if match else ""


def extract_meta_description(html: str) -> str:
    match = re.search(
        r'<meta\s+[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\'][^>]*>',
        html,
        re.IGNORECASE,
    )
    return clean(match.group(1)) if match else ""


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def fetch(url: str) -> dict:
    req = request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with request.urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            content_type = response.headers.get("content-type", "")
            status = response.status
            text = ""
            if "text/html" in content_type.lower():
                raw = response.read()
                charset = response.headers.get_content_charset() or "utf-8"
                text = raw.decode(charset, errors="replace")
            return {
                "url": url,
                "status": status,
                "ok": 200 <= status < 400,
                "contentType": content_type,
                "title": extract_tag(text, "title"),
                "h1": extract_tag(text, "h1"),
                "description": extract_meta_description(text),
            }
    except URLError as error:
        return {"url": url, "ok": False, "error": str(error.reason)}
    except Exception as error:
        return {"url": url, "ok": False, "error": str(error)}


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scan-urls.py <urls.txt>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    urls = [
        line.strip()
        for line in input_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

    results = [fetch(url) for url in urls]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
