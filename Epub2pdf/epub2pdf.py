#!/usr/bin/env python3

import subprocess
from pathlib import Path

def convertEpubToPdf(epubFile, pdfFile):
    try:
        subprocess.run(['ebook-convert', epubFile, pdfFile])
        print(f"Converted {epubFile} to PDF")
    except Exception as e:
        print(f"Error converting {epubFile} to PDF: {e}")

def main():
    epubDir = "/home/dad/Books"

    for epubFile in Path(epubDir).glob("*.epub"):
        pdfFile = epubFile.with_suffix(".pdf")
        convertEpubToPdf(str(epubFile), str(pdfFile))

if __name__ == "__main__":
    main()

