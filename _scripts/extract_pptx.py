import sys
sys.stdout.reconfigure(encoding='utf-8')
try:
    from markitdown import MarkItDown
    md = MarkItDown()
    result = md.convert(r"C:\Users\Eg4m1\Downloads\!2026+华中科大+周潘 +学术背景.pptx")
    with open(r"C:\Users\Eg4m1\Desktop\nswm-lab.github.io\_scripts\pptx_content.txt", 'w', encoding='utf-8') as f:
        f.write(result.text_content)
    print("PPTX extracted successfully")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
