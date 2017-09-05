#!/usr/bin/env python
# -*- coding: utf-8 -*-

# função que verifica se o programa está infectado
def infected(path, pathInfected):
    # score conta as chamadas diferentes
    # total conta o número de chamadas do arquivo
    score, total = 0, 0

    # abre o arquivo sadio para leitura
    file = open(path, "r")

    # abre o arquivo infectado para leitura
    fileInfected = open(pathInfected, "r")

    # percorerá todo o arquivo infectado, após o arquivo sadio ser percorrido
    for lineInfe in fileInfected:
        # essa flag será utilizada quando for encontrado linhas iguais
        flag = False
        # percorerá todo o arquivo sadio
        for line in file:
            # compara a linha do infectado com a linha do sadio
            if line == lineInfe:
                # se as linhas forem iguais a flag passa a ser verdadeira
                flag = True
                break
            # se a flag estiver falsa incrementa o score, já que não foi encontrada a linha no sadio
            if flag == False:
                score += 1

                # conta o total de chamadas
        total += 1

        # converte o total em ponto flutuante para que se possa ter o resultado da divisão um número não inteiro
    total = total / 1.0
    # probabilidade do programa estar infectado
    print(score / total) * 100, "%"


# função que gera as janelas
def sliding_window(path, name):
    # começo da janela
    begin = 0
    # final da janela
    end = 10

    # conta o numero de system calls no arquivos
    num_lines_file = sum(1 for line in open(path))
    # numero de conjuntos de 10
    number_of_windows = num_lines_file - 10 + 1

    i = 1
    # loop ate vc atingir o numero de conjuntos de 10 que vc quer
    while i <= number_of_windows:
        # abre o arquivo para leitura
        input_file = open(path, "r")
        # abri o arquivo para add (desse jeito vc sempre poe no final a nova entrada)
        output_file = open("window-" + name + ".txt", "a")
        # cria um array vazio
        result = []

        # for para ler cada linha do arquivo e uma variavel j que vai receber o valor da linha do arquivo
        for j, line in enumerate(input_file):
            # se a linha tiver entre a sua janela
            if begin <= j < end:
                # add ela ao array (removendo o \n da linha)
                result.append(line.rstrip())

                # junta todas as entradas do array em uma string separada por espaco
        result = " ".join(result)
        # escreve a string para seu arquivo
        output_file.write(result + "\n")
        # fecha o arquivo
        input_file.close()
        # fecha o arquivo
        output_file.close()
        # incrementa o i e a janela
        i += 1
        begin += 1
        end += 1


# abre o arquivo ls para escrita
output = open("mv.txt", "w")
# abre o arquivo ls sem os id para escrita
outputWithoutID = open("mv-without-id.txt", "w")
# abre o arquivo grep para escrita
outputGrep = open("cp.txt", "w")
# abre o arquivo grep semos id para escrita
outputGrepWithoutID = open("cp-without-id.txt", "w")

# abre o primeiro arquivo ls gerado
with open("log_cp.txt") as file:
    # percore cada linha do arquivo
    for line in file:
        # escreve apenas o id e a system call do arquivo ls em outro arquivo
        output.write(str(line.split("(")[0]) + "\n")
        # escreve apenas as system call de ls em outro arquivo
        outputWithoutID.write(line[:line.find("(")].split(" ")[1] + '\n')

        # fecha o arquivo
file.close()
# fecha o arquivo
output.close()

with open("log_mv.txt") as file:
    # abre o primeiro arquivo grep gerado
    for line in file:
        # escreve apenas o id e a system call do arquivo grep em outro arquivo
        outputGrep.write(line.split("(")[0] + "\n")
        # escreve apenas as system call de ls em outro arquivo
        outputGrepWithoutID.write(line[:line.find("(")].split(" ")[1] + '\n')

        # fecha o arquivo
file.close()
# fecha o arquivo
outputGrep.close()
# fecha o arquivo
outputWithoutID.close()
# fecha o arquivo
outputGrep.close()
# fecha o arquivo
outputGrepWithoutID.close()

# chama a função que gera as janelas de ls
sliding_window("mv-without-id.txt", "mv")
# chama a função que gera as janelas de grep
sliding_window("cp-without-id.txt", "cp")
# chama a função que detecta se o programa está infectado
infected("window-cp.txt", "window-mv.txt")
