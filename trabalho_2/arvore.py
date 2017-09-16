def clear(file):
    with open(file, "r+") as arq:
        if len(arq.readline()) > 0:
            arq.truncate()
# gera o n_gram
def create_gram(n, calls, gram):
    with open(calls, "r") as file1, open(gram, "a") as arq1:
        clear(gram)
        data = [x[:-1] for x in file1]
        for i in range(len(data) - n + 1):
            arq1.write(str(data[i:i + n])[1:-1].replace("\'", "") + "\n")
            # print(str(data[i:i + n])[1:-1].replace("\'", "") + "\n")

# gera o gram de 1 ate n
def gerar_gram(n):
    for j in range(1, n, 1):
        create_gram(j, "teste_cp_without_id.txt", "teste.txt")

class Arvore:

    def make_trie(self, file_gram):
        root = {}
        with open(file_gram, "r") as file:

            for line in file:
                current_dict = root
                array_words = line.rstrip().split(" ")
                for word in array_words:
                    current_dict = current_dict.setdefault(word, {})
            return root

# Depth First Search
def busca(tree, file):
    dict = tree.make_trie(file)
    for word in dict:
        print (str(word) + str(dict[word]))

def main():

    gerar_gram(12)
    arv = Arvore()
    busca(arv, "arquivo.txt")
    # print (dict)

if __name__ == "__main__":
    main()