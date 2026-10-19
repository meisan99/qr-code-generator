# QR Code Generator

Generate a QR code PNG from a link, using either a web UI or the command line.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

## Usage

### Web UI (Streamlit)

```bash
streamlit run app.py
```

Paste a link, optionally customize colors, box size, border and error correction, then download the PNG.

### Command line

```bash
python main.py https://example.com -o example.png
```

Options:

| Flag | Description | Default |
| ---- | ----------- | ------- |
| `-o`, `--output` | Output PNG path | `qrcode.png` |
| `--box-size` | Pixels per module | `10` |
| `--border` | Quiet-zone width in modules | `4` |
| `--fill` | Foreground color | `black` |
| `--back` | Background color | `white` |

## Project structure

- `qr_generator.py` – core QR generation and URL validation
- `app.py` – Streamlit UI
- `main.py` – command-line interface
