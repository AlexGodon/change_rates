"""Tool.

Usage:
  add_company_to_file.py (-c company)

  add_company_to_file.py (-h | --help)

Options:
  -h --help                                                 Show this screen.
  -c company --company=company                              Company name to add to file.
"""
from docopt import docopt
import logging
from shutil import copy
import os


def main():
    arguments = docopt(__doc__, version='Tools')
    company_name = arguments['--company']
    base_path = '../excel_files_source/'
    new_path = '../excel_files_renamed/'
    _, _, found_excel_files = next(iter(os.walk(base_path)))

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for excel_file in found_excel_files:
        copy(os.path.join(base_path, excel_file),
             os.path.join(new_path, '{}_{}'.format(company_name, excel_file)))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s %(levelname)s - %(message)s'
    )
    main()
