import pdfplumber
import sys

sys.stdout.reconfigure(encoding='utf-8')

with pdfplumber.open(r'C:\Users\Eg4m1\Downloads\Pan Zhou-cv-reverse-ordered.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            print(f'=== Page {i+1} ===')
            print(text)
            print()