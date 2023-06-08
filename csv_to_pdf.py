import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def csv_to_pdf(csv_file, pdf_file):
    # Read the CSV data
    df = pd.read_csv(csv_file)

    # Create a PDF object
    pdf_pages = PdfPages(pdf_file)

    # For each row in the DataFrame, create a bar chart
    for i, row in df.iterrows():
        # Create a figure
        fig = plt.figure()

        # Create a bar chart of the data
        row.plot(kind='bar')

        # Add the figure to the PDF
        pdf_pages.savefig(fig)

    # Close the PDF
    pdf_pages.close()

# Test the function
csv_to_pdf('test.csv', 'test.pdf')