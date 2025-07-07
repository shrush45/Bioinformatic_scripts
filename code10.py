##Overlap Graphs 

def overlap_graphs(filepath):
    with open(filepath,"r") as f:
        seq = []
        data = f.readlines()
        for line in data:
            if line.startswith('>')==False:
                # print(line)
                seq.append(line.strip())
        print(seq)
    
    score_all = []
    for i in range(len(seq)-1):
        print("i",seq[i])
        for j in range(len(seq)):
            print("j",seq[j])
        
                
    return score_all

filepath = "seq.fasta"
print(overlap_graphs(filepath))