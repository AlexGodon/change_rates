"""Main Change Rates.

Usage:
  main.py (-c company)

  main.py (-h | --help)

Options:
  -h --help                                                 Show this screen.
  -c company --company=company                              Company name to add to file.
"""
from docopt import docopt
from etl.companies import *
import logging
import os


def main():
    # arguments = docopt(__doc__, version='Main')
    base_path = 'excel_files_renamed/'
    source_path = 'excel_files_source/'
    destination_path = 'excel_files_destination/'

    if not os.path.exists(base_path) or not os.path.exists(source_path) or not os.path.exists(destination_path):
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        if not os.path.exists(source_path):
            os.makedirs(source_path)
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        logging.info('Directories Created, please re-run')
        exit(0)

    company_transformer = Transformer()
    for (dir_path, dir_names, found_excel_files) in os.walk(base_path):
        found_excel_files = sorted(found_excel_files)
        for excel_file in found_excel_files:
            company = excel_file.split('_')[0]
            try:
                eval('company_transformer.{}(company)'.format(company))
            except Exception as e:
                logging.error('An Error was found: {}'.format(e))
            break

            # data = pd.read_excel(os.path.join(base_path, excel_file), parse_dates=False, dtype='object')
            #TODO POC of having a dynamic company name linked the class defined.


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s %(levelname)s - %(message)s'
    )
    main()
