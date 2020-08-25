from PyPDF2 import PdfFileMerger
from os import listdir

"""
    The code expect that the pdf files are prefixed with numeric values to force the required order of merging, for example, the file doc_file.pdf should be renamed as 2-doc_file.pdf if it is required to merge it secondly.
"""

filesDir = input("Please, input the absolute path of the pdf files' directory:")

# make sure that the entered path ends with /
if filesDir[-1] != '/':
    filesDir += '/'

# exclude any non-pdf file
mergeList = [file for file in listdir(filesDir) if file.endswith('.pdf')]

# sort the pdf files depending on the added numerical prefix
mergeList.sort(key = lambda file: int(file.split('-')[0]))

# get a merger object
merger = PdfFileMerger()

# merge sequentially
for file in sortedList:
    merger.append(filesDir + file)

merger.write(filesDir + "/merged_file.pdf") # the output
merger.close()

