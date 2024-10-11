import os
import argparse
import pandas as pd

from PyPDF2 import PdfReader
from glob import glob


def check_file(fullfile):
    with open(fullfile, 'rb') as f:
        try:
            pdf = PdfReader(f)
            info = pdf.metadata
            if info:
                return True
            else:
                return False
        except Exception as e:
            return False


def search_files(dirpath: str, isRecursive: bool) -> pd.DataFrame:
    pwdpath = os.path.dirname(os.path.realpath(__file__))
    print("Running path : %s\n" %pwdpath)
    files = []

    if os.access(dirpath, os.R_OK):
        for fullfile in glob(dirpath + '/**/*.pdf', recursive=isRecursive):
            filename = os.path.basename(fullfile)
            if not check_file(fullfile):
                print("ERROR " + fullfile)
                files.append((filename, fullfile, 'corrupted'))
            # else:
            #     print("OK " + fullfile + "\n")
            #     files.append((filename, fullfile, 'good'))
    else:
        print("Path is not valid")

    df = pd.DataFrame(files, columns=['filename', 'fullpath', 'status'])
    return df


def main(args):
    df = search_files(args.dirpath, args.recursive)
    if args.output is not None:
        df.to_csv(args.output, index=False)
        print(f'\nFinal report saved to {args.output}')
    print(df['status'].value_counts())


if __name__ == '__main__':
    """ Command line script for finding corrupted PDFs in a directory. """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dirpath', type=str, required=True, help='Path to directory containing PDFs.')
    parser.add_argument('-o', '--output', type=str, required=False, help='Path to output CSV file.')
    parser.add_argument('-r', '--recursive', action='store_true', help='Read all files from the current directory and sub directories.')
    args = parser.parse_args()
    main(args)