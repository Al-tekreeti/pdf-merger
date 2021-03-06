# pdf-merger
Given a directory of pdf files, an output pdf file is generated by merging the pdf files according to a certain order. The code expect that the pdf files are prefixed with numeric values to force the required order of merging, for example, the file `doc_file.pdf` may be renamed as 2-doc_file.pdf if it is required to merge it secondly. The implemented logic is quite similar to that explained <a href=https://medium.com/@akhileshjoshi123/merge-pdfs-with-python-d4d3bfbdbd3b class="mw-redirect" title="Merge pdfs with python">in this article</a>.
# install
First download the package `pdf-merger-0.0.1.tar.gz`. Then, using `pip` package installer, the package is installed as follows:

<code> pip install pdf-merger </code>
 
# Usage
The code in `src\app.py` shows how to use the package to merge pdf files. The package is developed for Unix-like operating systems. When you run `app.py` by executing `python src/app.py`, the following message `Please, input the absolute path of the pdf files' directory:` is displayed to promot the user to input the absolute path of the pdf files directory. The output file from the merging process is located in the same directory of the input pdf files.
