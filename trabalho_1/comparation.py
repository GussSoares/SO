with open("syscalls/log_syscall_cp_without_id.txt", "r") as file1, open("syscalls/log_syscall_mv_without_id.txt", "r") as file2, open("result.txt", "w") as result:
    def compare(healthy, infected):
        data1 = [x[:-1] for x in healthy]
        data2 = [x[:-1] for x in infected]

        list1 = list(set(data1))
        list2 = list(set(data2))

        print ("Elements file 1: ", list1)
        print ("Elements file 2: ", list2)

        level_infection = len(set(data2) - set(data1)) / len(list2)*100

        print("Infection: ", level_infection, '%')

        result.write("Elements file 1: ")
        result.write(str(list1)+"\n")
        result.write("Elements file 2: ")
        result.write(str(list2)+"\n")
        result.write("Infection: ")
        result.write(str(level_infection)+"%")

    compare(file1, file2)