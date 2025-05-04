##Reverse complement of a DNA/RNA string

def reverseComplement(seq):
    complement = {'A':'T','T':'A','C':'G','G':'C','N':'N'}
    t = ''
    for base in seq:
        t = complement[base] + t
    return t 
seq = input("Enter a sequence:")
print("The reverse compliment of a sequence is :",reverseComplement(seq.upper()))

