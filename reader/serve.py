#!/usr/bin/env python3
"""Build the reader and serve it locally."""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import webbrowser
from pathlib import Path

from build import OUT_DIR, build

ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve F1 Time Capsule reader")
    parser.add_argument("--port", type=int, default=4321)
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()

    build(base="/")
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT_DIR))
    with socketserver.TCPServer(("127.0.0.1", args.port), handler) as httpd:
        url = f"http://127.0.0.1:{args.port}/"
        print(f"Serving {OUT_DIR} at {url}")
        if not args.no_open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
