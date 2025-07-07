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
        count = 0
        for j in range(0,len(seq[i])):
            if seq[i][j] == seq[i+1][j]:
                print(seq[i][j],seq[i+1][j],"True")
                count+=1
            else:
                print(False)
                count+=0
            # print(seq[i][j])
        score_all.append(count)
        count = 0
    return score_all

filepath = "seq.fasta"
print(overlap_graphs(filepath))