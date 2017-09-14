def _create_gram(n, file="teste_cp_without_id.txt", arq="n_gram_cp.txt"):
    with open(file, "r") as file1, open(arq, "w") as arq1:
        data = [x[:-1] for x in file1]
        for i in range(len(data) - n + 1):
            arq1.write(str(data[i:i+n])[1:-1].replace("\'","") + "\n")
            print (str(data[i:i+n])[1:-1].replace("\'","") + "\n")

for n in range (1,11,1):
    _create_gram(n, file="teste_cp_without_id.txt", arq="n_gram_cp.txt")
