
#This function creates a log file that contains the id and system calls, of the commands cp and mv
def _create_log_file(file="log_cp.txt",arq="teste_cp.txt"):
    with open(file,"r") as file1:
        with open(arq,"w") as arq1:
            for line in file1:
                result = line.split("(")[0]
                if result[1] != "+":
                    arq1.write(result+"\n")
                    print(result)

#_create_log_file(file="log_cp.txt", arq="teste_cp.txt")

#This function creates a log file that contains the system calls, of the commands cp and mv
def _create_log_without_id(file="teste_cp.txt",arq="teste_cp_without_id.txt"):
    with open(file) as file1, open(arq, "w") as arq1:
        for line in file1:
            result = line.split("] ")[1]
            if result[1] != "+":
                arq1.write(result)
                print(result)

#_create_log_without_id(file="teste_cp.txt", arq="teste_cp_without_id.txt")

#This function creates a n-grams file of the syscalls of the commands cp and mv
def _create_gram(n, file="log_syscall_mv_without_id.txt", arq="n_gram_mv.txt"):
    with open(file, "r") as file1, open(arq, "w") as arq1:
        data = [x[:-1] for x in file1]
        for i in range(len(data) - n + 1):
            arq1.write(str(data[i:i+n])[1:-1].replace("\'","") + "\n")

#_create_gram(10, file="log_syscall_mv_without_id.txt", arq="n_gram_mv.txt")

#This function does a comparation between two files, healthy and infected
def _compare(healthy="n_gram_cp.txt", infected="n_gram_mv.txt"):
    with open(healthy, "r") as arq_healthy, open(infected, "r") as arq_infected:

        arq1 = [z[:-1] for z in arq_healthy]
        arq2 = [y[:-1] for y in arq_infected]
        inter = set(arq1).intersection(arq2)
        list = [x[:-1] for x in inter]

        print("Elements file1: "+str(arq1)+"\n")
        print("Elements file2: "+str(arq2)+"\n")
        print("Infection: "+str(100-(len(list) / len(arq2))*100) + "%")

_compare(healthy="n_gram_cp.txt", infected="n_gram_mv.txt")