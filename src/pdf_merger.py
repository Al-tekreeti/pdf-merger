from PyPDF2 import PdfFileMerger
from os import listdir

class PdfMerger:
    """
    A class used to merge pdf files contained in a directory

    ...

    Attributes
    ----------
    filesDir : str
        an absolute path to the pdf files directory
    merger : object
        an instantiated object of the class PyPDF2.PdfFileMerger

    Methods
    -------
    pdf_merge()
        returns an absolute path to the output file 
    merger_close()
        frees the self.merger object
    """
    def __init__(self, filesDir, outFile = "merged_file.pdf"):
        """
        Parameters
        ----------
        filesDir : str
            an absolute path to the pdf files directory
        merger : object
            an instantiated object of the class PyPDF2.PdfFileMerger
        outFile : str
            an output file name with pdf extention
        """
        # make sure that the entered path ends with /
        if filesDir[-1] != '/':
            self.filesDir = filesDir + '/'
        else:
            self.filesDir = filesDir

        # output file name
        self.outFile = outFile

        # get a merger object
        self.merger = PdfFileMerger()

    def pdf_merge(self):
        """Returns the name and the absolute path of the output file

        Parameters
        ----------
        None

        Returns
        -------
        a string of the full path of the output file
        """
        # exclude any non-pdf file
        mergeList = [file for file in listdir(self.filesDir) if file.endswith('.pdf')]

        # sort the pdf files depending on the added numerical prefix
        mergeList.sort(key = lambda file: int(file.split('-')[0]))

        # merge sequentially
        for file in mergeList:
            self.merger.append(self.filesDir + file)

        self.merger.write(self.filesDir + self.outFile) # the output
        return self.filesDir + self.outFile
    
    def merger_close(self):
        """Frees the object merger that is derived from PdfFileMerger class

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.merger.close()
