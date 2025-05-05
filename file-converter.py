import sys
import markdown

def validate_args(expected_args):
    if len(sys.argv) < expected_args:
        print(f"Error: Expected at least {expected_args} arguments, but got {len(sys.argv)}.")
        sys.exit(1)

# コマンドとファイルパスの取得
if len(sys.argv) < 3:
    print("Usage:")
    print(" file-converter.py markdown <inputfile> <outputfile>")
    sys.exit(1)
        
inputfile = sys.argv[2]
outputfile = sys.argv[3]

if sys.argv[1] == 'markdown':
    validate_args(4)
    with open(inputfile) as f:
        contents = f.read()
    f.closed
        
    html = markdown.markdown(contents)
    
    with open(outputfile, 'w') as f:
        f.write(html)
    f.closed
