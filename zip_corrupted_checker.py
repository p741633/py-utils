"""Module providing a function finding currupted zip."""

import os
import argparse
import zipfile
from glob import glob
import pandas as pd


def check_file(fullfile):
    """Function check zip file."""
    with open(fullfile, "rb") as f:
        try:
            the_zip_file = zipfile.ZipFile(f)
            info = the_zip_file.testzip()
            if info is not None:
                return False
            return True
        except FileNotFoundError as e:
            print(f"ERROR {fullfile} : File not found - {e}")
            return False
        except PermissionError as e:
            print(f"ERROR {fullfile} : Permission denied - {e}")
            return False
        # pylint: disable=broad-exception-caught
        except Exception as e:
            print(f"ERROR {fullfile} : Unexpected error - {e}")
            return False


def search_files(dirpath: str, is_recursive: bool) -> pd.DataFrame:
    """Function search zip file."""
    pwdpath = os.path.dirname(os.path.realpath(__file__))
    print(f"Running path : {pwdpath}\n")
    files = []

    if os.access(dirpath, os.R_OK):
        for fullfile in glob(dirpath + "/**/*.zip", recursive=is_recursive):
            filename = os.path.basename(fullfile)
            if not check_file(fullfile):
                print("ERROR " + fullfile)
                files.append((filename, fullfile, "corrupted"))
            # else:
            #     print("OK " + fullfile + "\n")
            #     files.append((filename, fullfile, 'good'))
    else:
        print("Path is not valid")

    df = pd.DataFrame(files, columns=["filename", "fullpath", "status"])
    return df


def main(args):
    """Function main."""
    df = search_files(args.dirpath, args.recursive)
    if args.output is not None:
        df.to_csv(args.output, index=False)
        print(f"\nFinal report saved to {args.output}")
    print(df["status"].value_counts())


if __name__ == "__main__":
    print("Command line script for finding corrupted ZIPs in a directory.")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dirpath",
        type=str,
        required=True,
        help="Path to directory containing ZIPs.",
    )
    parser.add_argument(
        "-o", "--output", type=str, required=False, help="Path to output CSV file."
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Read all files from the current directory and sub directories.",
    )
    input_parameter = parser.parse_args()
    main(input_parameter)
