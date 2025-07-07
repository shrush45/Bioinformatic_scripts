##Computing GC content
from packages.biopackage import valid_seq

def calculate_gc(seq):
    n = len(seq)
    count=0
    for i in seq.upper():
        if i=='G' or i=='C':
            count+=1
    gc_count = (count/n)*100
    return gc_count

seq = input("Enter sequence:")
if valid_seq(seq)==True:
    print(calculate_gc(seq))
else:
    print("Enter valid sequence")    