import os
import pandas as pd
from tabulate import tabulate
from fpdf import FPDF

from src.src_utils import *


class Reports:
    def __init__(self, file_name):
        self.file_name = file_name

    def gen_reports(self):

        filepath = report_output_folder_path + self.file_name

        def parse_csv(filepath, columns):
            df = pd.read_csv(filepath, usecols=columns)
            return df

        def generate_table(dataframe):
            # Use tabulate to format the dataframe as a table string
            table = tabulate(dataframe, headers='keys', tablefmt='grid')
            return table

        def save_table_as_pdf(table, output_file):
            # Create an instance of FPDF class
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()

            # Set font
            pdf.set_font("Arial", size=12)

            # Add each line of the table to the PDF
            for line in table.split("\n"):
                pdf.cell(200, 10, txt=line, ln=True)

            # Save the PDF to the specified output file
            pdf.output(output_file)


        def csv_to_pdf(filepath, output_pdf, selected_columns):
            # Parse CSV and select fields
            dataframe = parse_csv(filepath, selected_columns)

            # Generate the table
            table = generate_table(dataframe)

            # Save the table as a PDF
            save_table_as_pdf(table, output_pdf)

        # Example usage
        file_name_with_ext = filepath.split('/')[-1]
        output_pdf = os.path.join(output_pdf_path, file_name_with_ext.split(".")[0] + '.pdf')  # Output PDF file path
        selected_columns = [selected_timestamp, selected_elapsed, selected_latency]  # Specify columns to include
        # calling function
        csv_to_pdf(filepath, output_pdf, selected_columns)