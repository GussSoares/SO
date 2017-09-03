import string
import itertools
import re

with open("teste2.txt", "r") as file:
	with open("teste_novo.txt", "w") as arq:
		for x in range(1,10):
			for line in itertools.islice(file, 0, 10):
				r = re.search("[<].*[>]", file)
				r.group(0)
				result = string.replace(r.group(0), "")
				print (result)
				arq.write(result)
			arq.write("\n\n")