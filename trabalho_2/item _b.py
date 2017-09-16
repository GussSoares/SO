class Gram:

    def create_gram(n, file="teste_cp_without_id.txt", arq="n_gram_cp.txt"):
        with open(file, "r") as file1, open(arq, "w") as arq1:
            data = [x[:-1] for x in file1]
            for i in range(len(data) - n + 1):
                arq1.write(str(data[i:i+n])[1:-1].replace("\'","") + "\n")
                print (str(data[i:i+n])[1:-1].replace("\'","") + "\n")

    def gerar_gram(self, n):
        for j in range (1,n,1):
            self.create_gram(j, file="teste_cp_without_id.txt", arq="n_gram_cp.txt")
