import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
import barcode
from barcode.writer import ImageWriter

st.set_page_config(page_title="QR & Barcode Generator", page_icon="🔳")

st.title("🔳 QR & Barcode Generator")

# User input
data = st.text_input("Enter the data for the code", "https://example.com")

code_type = st.radio("Select Code Type", ("QR Code", "Barcode"))

if st.button("Generate"):
    if code_type == "QR Code":
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buf = BytesIO()
        img.save(buf)
        buf.seek(0)

        st.image(Image.open(buf), caption="Generated QR Code", use_column_width=True)

        st.download_button("📥 Download QR Code", data=buf, file_name="qr_code.png", mime="image/png")

    elif code_type == "Barcode":
        # Using Code128 which supports full ASCII
        CODE128 = barcode.get_barcode_class('code128')
        bar = CODE128(data, writer=ImageWriter())

        buf = BytesIO()
        bar.write(buf)
        buf.seek(0)

        st.image(Image.open(buf), caption="Generated Barcode", use_column_width=True)

        st.download_button("📥 Download Barcode", data=buf, file_name="barcode.png", mime="image/png")
