"""Command-line usage: python main.py https://example.com -o example.png"""

import argparse
import sys

from qr_generator import generate_qr, is_valid_url


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a QR code PNG from a link.")
    parser.add_argument("link", help="URL to encode (http or https)")
    parser.add_argument("-o", "--output", default="qrcode.png", help="Output PNG path")
    parser.add_argument("--box-size", type=int, default=10, help="Pixels per module")
    parser.add_argument("--border", type=int, default=4, help="Quiet-zone width in modules")
    parser.add_argument("--fill", default="black", help="Foreground color")
    parser.add_argument("--back", default="white", help="Background color")
    args = parser.parse_args()

    if not is_valid_url(args.link):
        print(f"Error: '{args.link}' is not a valid http(s) URL.", file=sys.stderr)
        return 1

    image = generate_qr(args.link, args.box_size, args.border, args.fill, args.back)
    image.save(args.output)
    print(f"Saved QR code to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
