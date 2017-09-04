import string

def create_gram(n):
    with open("syscalls/log_syscall_mv_without_id.txt", "r") as file:
        with open("syscalls/n_gram_mv.txt", "w") as arq:
            data = [x[:-1] for x in file]
            # print (data)
            for i in range(len(data) - n + 1):
                teste = arq.write(str(data[i:i+n])[1:-1].replace("\'","") + "\n")

create_gram(10)