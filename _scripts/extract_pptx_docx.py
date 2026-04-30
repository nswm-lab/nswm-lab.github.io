import sys
sys.stdout.reconfigure(encoding='utf-8')
import zipfile
import xml.etree.ElementTree as ET

# PPTX extraction
try:
    prs_path = r"C:\Users\Eg4m1\Downloads\!2026+华中科大+周潘 +学术背景.pptx"
    text_content = []
    with zipfile.ZipFile(prs_path, 'r') as z:
        slide_files = sorted([f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')])
        for slide_file in slide_files:
            tree = ET.parse(z.open(slide_file))
            root = tree.getroot()
            ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            texts = [t.text for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if t.text]
            if texts:
                text_content.append(' | '.join(texts))
    with open(r"C:\Users\Eg4m1\Desktop\nswm-lab.github.io\_scripts\pptx_content.txt", 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(text_content))
    print(f"PPTX: {len(slide_files)} slides extracted")
except Exception as e:
    print(f"PPTX Error: {e}")

# DOCX extraction
try:
    docx_path = r"C:\Users\Eg4m1\Downloads\！20260401+其它+F.docx"
    text_content = []
    with zipfile.ZipFile(docx_path, 'r') as z:
        doc_xml = z.read('word/document.xml')
        tree = ET.fromstring(doc_xml)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        texts = [t.text for t in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
        text_content = ' '.join(texts)
    with open(r"C:\Users\Eg4m1\Desktop\nswm-lab.github.io\_scripts\docx_content.txt", 'w', encoding='utf-8') as f:
        f.write(text_content)
    print("DOCX extracted successfully")
except Exception as e:
    print(f"DOCX Error: {e}")
