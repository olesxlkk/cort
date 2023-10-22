A = 0
B = -1
def slicer(w, q):
    fir = sec = A   
    if q in w:
        fir = w.index(q)
    if w.count(q) > 1:
        sec = w.index(q, fir + 1) + 1
    else:
        sec = B
    return w[fir:sec]