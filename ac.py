def inicializar():
	tab = []
	for i in range(3):
		linha = []
		for j in range(3):
			linha.append(".")
		tab.append(linha)
	return tab

def main():
	atividade = inicializar()
	print(atividade)

if __name__ == "__main__":
	main()
