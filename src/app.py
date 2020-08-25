from PyPDF2 import PdfFileMerger
from os import listdir

"""
    The code expect that the pdf files are prefixed with numeric values to force the required order of merging, for example, the file doc_file.pdf should be renamed as 2-doc_file.pdf if it is required to merge it secondly.
"""
filesDir = input("Please, input the absolute path of the pdf files' directory:")

mergeList = []

# exclude any non-pdf file
for file in listdir(filesDir):
    if not file.endswith('.pdf'):
        continue
    mergeList.append(filesDir + file)

# get a merger object
merger = PdfFileMerger()

# sort the pdf files depending on the added numerical prefix
sortedList = mergeList.sort(key = lambda file: int(file.split('-')[0]))

# merge sequentially
for file in sortedList:
    merger.append(file)

merger.write(filesDir + "/merged_file.pdf") # the output
merger.close()

