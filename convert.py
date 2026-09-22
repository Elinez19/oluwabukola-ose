import sys
import fitz  # PyMuPDF

def convert_pdf_to_png(pdf_path, png_path):
    print(f"Converting {pdf_path} to {png_path}...")
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # first page
        pix = page.get_pixmap(dpi=150)
        pix.save(png_path)
        print("Success")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    convert_pdf_to_png("assets/certs/CERTIFIED IN CYBERSECURITY - ISC2.pdf", "assets/certs/isc2-cybersecurity.png")
    convert_pdf_to_png("assets/certs/IBM - System Analyst Professional Certificate.pdf", "assets/certs/ibm-system-analyst.png")
    convert_pdf_to_png("assets/certs/Certified Cybersecurity Professional Educator CCEP.pdf", "assets/certs/ccep-educator.png")
    convert_pdf_to_png("assets/certs/Introduction-to-AI-Security-Certificate.pdf", "assets/certs/intro-to-ai-security.png")
