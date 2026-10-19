"""Core QR code generation, shared by the CLI (main.py) and the Streamlit UI (app.py)."""

from io import BytesIO
from urllib.parse import urlparse

import qrcode
from qrcode.constants import (
    ERROR_CORRECT_H,
    ERROR_CORRECT_L,
    ERROR_CORRECT_M,
    ERROR_CORRECT_Q,
)

# Higher levels survive more damage/obstruction (e.g. a logo on top) but make denser codes.
ERROR_CORRECTION = {
    "L (7%)": ERROR_CORRECT_L,
    "M (15%)": ERROR_CORRECT_M,
    "Q (25%)": ERROR_CORRECT_Q,
    "H (30%)": ERROR_CORRECT_H,
}


def is_valid_url(link: str) -> bool:
    parsed = urlparse(link.strip())
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def generate_qr(
    link: str,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
    error_correction: str = "M (15%)",
):
    """Return a PIL image of the QR code for `link`."""
    qr = qrcode.QRCode(
        version=None,  # let the library pick the smallest size that fits
        error_correction=ERROR_CORRECTION[error_correction],
        box_size=box_size,
        border=border,
    )
    qr.add_data(link.strip())
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")


def to_png_bytes(image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()
