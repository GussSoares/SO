import string

with open("log_mv_without_id.txt") as file:
    with open("log_syscall_mv_with_id.txt", "w") as arq:
        for line in file:
            result = line.split("(")[0]
            if result[1] != "+":
                arq.write(result+"\n")
                print(result)
