# Python Utilities

- pdf-corrupted-checker.py
  - Checks if a PDF file is corrupted. It uses the PyPDF2 library.
- zip_corrupted_checker.py
  - Checks if a ZIP file is corrupted. It uses the zipfile library.
- rar_corrupted_checker.py
  - Checks if a RAR file is corrupted. It uses the patoolib library.

## How to use

Example : python rar_corrupted_checker.py -d /{path} -r -o output.txt

    -d : Directory to check
    -r : Recursive check
    -o : Output file
