# HackerRank - Designer PDF Viewer

def designerPdfViewer(h, word):
    alp = dict(zip([chr(i) for i in range(97, 123)], h))
    return len(word) * alp[max(word, key=lambda x: alp[x])]
