

def _compare(healthy="syscalls/n_gram_cp.txt", infected="syscalls/n_gram_mv.txt"):
    with open(healthy, "r") as arq_healthy, open(infected, "r") as arq_infected:

        arq1 = [z[:-1] for z in arq_healthy]
        arq2 = [y[:-1] for y in arq_infected]
        inter = set(arq1).intersection(arq2)
        list = [x[:-1] for x in inter]

        print(arq1)
        print(arq2)

        print(len(list))

        print(100-(len(list) / len(arq2))*100, "%")

_compare(healthy="syscalls/n_gram_cp.txt", infected="syscalls/n_gram_mv.txt")