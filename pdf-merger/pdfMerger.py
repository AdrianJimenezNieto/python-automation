import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

def mergePDF():
  for file in os.listdir(os.curdir):
    if file.endswith(".pdf") & (file != "combinedDocs.pdf"):
      print(file)
      merger.append(file)
  merger.write("combinedDocs.pdf")
  merger.close()

if __name__ == "__main__":
  mergePDF()