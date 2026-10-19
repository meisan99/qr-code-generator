"""Streamlit UI: streamlit run app.py"""

""".venv\Scripts\streamlit run app.py"""

import streamlit as st

from qr_generator import ERROR_CORRECTION, generate_qr, is_valid_url, to_png_bytes

st.set_page_config(page_title="QR Code Generator", page_icon="🔳", layout="centered")

st.title("QR Code Generator")
st.caption("Paste a link and get a QR code you can download as PNG.")

link = st.text_input("Link", placeholder="https://example.com")

with st.expander("Customize"):
    col1, col2 = st.columns(2)
    with col1:
        fill_color = st.color_picker("Foreground", "#000000")
        box_size = st.slider("Box size (px per module)", 4, 20, 10)
    with col2:
        back_color = st.color_picker("Background", "#FFFFFF")
        border = st.slider("Border (modules)", 1, 10, 4)
    error_correction = st.selectbox(
        "Error correction",
        list(ERROR_CORRECTION),
        index=1,
        help="Higher levels still scan when part of the code is damaged or covered.",
    )

if link:
    if not is_valid_url(link):
        st.error("Please enter a valid URL starting with http:// or https://")
    else:
        image = generate_qr(
            link, box_size, border, fill_color, back_color, error_correction
        )
        png = to_png_bytes(image)

        st.image(png, caption=link, width=300)
        st.download_button(
            "Download PNG", data=png, file_name="qrcode.png", mime="image/png"
        )
else:
    st.info("Enter a link above to generate a QR code.")
