# HackerRank - Designer PDF Viewer
# Problem: Designer PDF Viewer
# Source: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Note: Calculates the highlighted area using the tallest letter in the word multiplied by the word's length.
def designerPdfViewer(h, word):
    alp = dict(zip([chr(i) for i in range(97, 123)], h))
    return len(word) * alp[max(word, key=lambda x: alp[x])]
