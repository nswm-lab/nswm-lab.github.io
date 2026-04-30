import pdfplumber
import sys

sys.stdout.reconfigure(encoding='utf-8')

with pdfplumber.open(r'C:\Users\Eg4m1\Downloads\Pan Zhou-cv-reverse-ordered.pdf') as pdf:
    all_text = []
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            all_text.append(f'=== Page {i+1} ===\n{text}')
    
    with open(r'C:\Users\Eg4m1\Desktop\nswm-lab.github.io\_scripts\cv_content.txt', 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(all_text))
    print(f'Written {len(pdf.pages)} pages to cv_content.txt')
