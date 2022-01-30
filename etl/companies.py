import pandas as pd
from os import walk, path, fwalk
from main import logging


class Transformer:
    def __init__(self):
        self.base_path = 'excel_files_renamed'
        self.source_path = 'excel_files_source'
        self.destination_path = 'excel_files_destination'

    def open_excel_files(self, company):
        try:
            _, _, found_excel_files = next(iter(walk('{}'.format(self.base_path))))
        except StopIteration:
            logging.error('No files were found in the directory: [{}]'.format(self.base_path))
            exit(1)
        data = pd.DataFrame()
        for excel_file in found_excel_files:
            file_name, file_ext = path.splitext(excel_file)
            if not file_name.startswith(company):
                continue
            if file_ext != '.xlsx':
                logging.info('Skipping the file [{}], as the file extension is not [.xlsx]'.format(excel_file))
                continue

            if data.empty:
                data = pd.read_excel(path.join(self.base_path, excel_file), dtype=object)
            else:
                # Todo concatenate the dataframes. Maybe, Andy you tell me ;)
                pass

        return data

    def humania(self, company):
        data = self.open_excel_files(company)
