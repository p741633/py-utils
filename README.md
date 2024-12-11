# Python Utilities

- `pdf-corrupted-checker.py`: Checks if a PDF file is corrupted. It uses the PyPDF2 library.
- `zip_corrupted_checker.py`: Checks if a ZIP file is corrupted. It uses the zipfile library.
- `rar_corrupted_checker.py`: Checks if a RAR file is corrupted. It uses the patoolib library.

## General Options:

```
python rar_corrupted_checker.py -d /folder -r -o ./output.csv
```

    -h, --help                      Print this help text and exit
    -d, --dirpath                   Directory to check
    -r, --recursive                 Recursive check
    -o, --output                    Output file (CSV)
