from pdf_merger import PdfMerger as PDF

"""
    The code expect that the pdf files are prefixed with numeric values to force the required order of merging, for example, the file doc_file.pdf may be renamed as 2-doc_file.pdf if it is required to merge it secondly.
"""

filesDir = input("Please, input the absolute path of the pdf files' directory:")

pdf = PDF(filesDir)
output_file = pdf.pdf_merge()

if __name__ == "__main__":
    print(f"The output pdf file is {output_file}")
