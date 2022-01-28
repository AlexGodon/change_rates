"""Main Change Rates.

Usage:
  main.py (-c company)

  main.py (-h | --help)

Options:
  -h --help                                                 Show this screen.
  -c company --company=company                              Company name to add to file.
"""
from docopt import docopt
import pandas as pd
import logging
import os


def main():
    # arguments = docopt(__doc__, version='Main')
    base_path = 'excel_files_renamed/'
    for (dir_path, dir_names, found_excel_files) in os.walk(base_path):
        found_excel_files = sorted(found_excel_files)
        for excel_file in found_excel_files:
            file_name, file_ext = os.path.splitext(excel_file)
            company = file_name.split('_')[0]
            if file_ext != '.xlsx':
                logging.info('Skipping the file [{}], as the file extension is not [.xlsx]'.format(excel_file))
                continue
            # data = pd.read_excel(os.path.join(base_path, excel_file), parse_dates=False, dtype='object')
            #TODO POC of having a dynamic company name linked the class defined.

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s %(levelname)s - %(message)s'
    )
    main()
