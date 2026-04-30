import sys
sys.stdout.reconfigure(encoding='utf-8')
try:
    from markitdown import MarkItDown
    md = MarkItDown()
    result = md.convert(r"C:\Users\Eg4m1\Downloads\！20260401+其它+F.docx")
    with open(r"C:\Users\Eg4m1\Desktop\nswm-lab.github.io\_scripts\docx_content.txt", 'w', encoding='utf-8') as f:
        f.write(result.text_content)
    print("DOCX extracted successfully")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
