import sys
from graph import *
from djikstra import *

def numberToName(auxList):
	for x, j in enumerate(auxList):
		if j == 0:
			auxList[x] = "PortoAlegre"
		if j == 1:
			auxList[x] = "Florianopolis"
		if j == 2:
			auxList[x] = "Curitiba"
		if j == 3:
			auxList[x] = "Sao Paulo"
		if j == 4:
			auxList[x] = "Rio de Janeiro"
		if j == 5:
			auxList[x] = "Vitoria"
		if j == 6:
			auxList[x] = "Campo Grande"
		if j == 7:
			auxList[x] = "Cuiaba"
		if j == 8:
			auxList[x] = "Belo Horizonte"
		if j == 9:
			auxList[x] = "Goiania"
		if j == 10:
			auxList[x] = "Brasilia"
		if j == 11:
			auxList[x] = "Salvador"
		if j == 12:
			auxList[x] = "Aracaju"
		if j == 13:
			auxList[x] = "Maceio"
		if j == 14:
			auxList[x] = "Recife"
		if j == 15:
			auxList[x] = "Joao Pessoa"
		if j == 16:
			auxList[x] = "Campina Grande"
		if j == 17:
			auxList[x] = "Natal"
		if j == 18:
			auxList[x] = "Fortaleza"
		if j == 19:
			auxList[x] = "Sao Luis"
		if j == 20:
			auxList[x] = "Belem"
		if j == 21:
			auxList[x] = "Palmas"
		if j == 22:
			auxList[x] = "Macapa"
		if j == 23:
			auxList[x] = "Manaus"
		if j == 24:
			auxList[x] = "Boa Vista"
		if j == 25:
			auxList[x] = "Porto Velho"
		if j == 26:
			auxList[x] = "Rio Branco"
		if j == 27:
			auxList[x] = "Teresina"
	return auxList

if __name__ == '__main__':

	infinito = 999999

	#graph declaration
	graph = Grafo()
	for i in range(28):
		graph.adicionaNodo(i)

	graph.criaAresta(0,1,10) #porto com floripa
	graph.criaAresta(0,2,10) #porto com curitiba
	graph.criaAresta(2,3,10) #curitiba com sao paulo
	graph.criaAresta(2,6,10) #curitiba com campo grande
	graph.criaAresta(6,7,10) #campo grande com cuiaba
	graph.criaAresta(7,25,3) #cuiaba com porto velho
	graph.criaAresta(25,26,3) #porto velho com rio branco
	graph.criaAresta(1,3,10) #florianopolis com sao paulo
	graph.criaAresta(3,4,10) #sao paulo com rio de janeiro
	graph.criaAresta(3,8,10) #sao paulo com belo horizonte
	graph.criaAresta(3,18,10) #sao paulo com fortaleza
	graph.criaAresta(4,5,10) #rio de janeiro com vitoria
	graph.criaAresta(4,10,10) #rio de janeiro com brasilia
	graph.criaAresta(5,11,20) #vitoria com salvador
	graph.criaAresta(8,10,10) #belo horizonte com brasilia
	graph.criaAresta(8,11,10) #belo hozionte com salvador
	graph.criaAresta(10,9,20) #brasilia com goiania
	graph.criaAresta(10,18,10) #brasilai com fortaleza
	graph.criaAresta(10,20,10) #brasilia com belem
	graph.criaAresta(9,7,10) #goiania com cuiaba
	graph.criaAresta(9,21,10) #goiania com palmas
	graph.criaAresta(11,12,10) #salvador com aracaju
	graph.criaAresta(11,14,10) #salvador com recife
	graph.criaAresta(12,13,10) #aracaju com maceio
	graph.criaAresta(13,14,10) #maceio com recife
	graph.criaAresta(14,27,3) #recife com teresina
	graph.criaAresta(14,16,10) #recife com campina grande
	graph.criaAresta(14,18,10) #recife com fortaleza
	graph.criaAresta(16,15,10) #campina grande com joao pessoa
	graph.criaAresta(15,17,10) #joao pessoa com natal
	graph.criaAresta(17,18,10) #natal com fortaleza
	graph.criaAresta(18,19,10) #fortaleza com sao luis
	graph.criaAresta(19,20,10) #sao luis com belem
	graph.criaAresta(27,20,3) #teresina com belem
	graph.criaAresta(20,22,1) #belem com macapa
	graph.criaAresta(20,23,1) #belem com manaus
	graph.criaAresta(21,20,10) #palmas com belem
	graph.criaAresta(10,23,1) #brasilia com manaus
	graph.criaAresta(23,24,1) #manaus com boa vista

	# receive arguments from command line
	if len(sys.argv) == 4:
		k = int(sys.argv[1])
		initial_node_number = int(sys.argv[2])
		dest_node_number = int(sys.argv[3])
		if initial_node_number>0 and dest_node_number<28:
			u = 0
			pathToSelf = False
			while u < k:
				if dest_node_number in graph.listaDeNodos:
					dijkstra = Dijkstra(graph, graph.listaDeNodos[initial_node_number].getNome(), graph.listaDeNodos[dest_node_number].getNome())
					if dijkstra.dictDistanciaDoNodoInicial[dest_node_number] < infinito and pathToSelf==False:
						minimunPathAux = list(dijkstra.minimunPathList)
						print "Shortest Path "+str(u+1) +": "+ str(numberToName(minimunPathAux))
						print "Path Total Weight: "+str(dijkstra.dictDistanciaDoNodoInicial[dest_node_number])
						graph.deletaMenorAresta(dijkstra.minimunPathList)
						if dijkstra.dictDistanciaDoNodoInicial[dest_node_number] == 0:
							pathToSelf = True
					else:
							u = k
							print "All Possible Paths Found"
				u = u+1
		else:
			print "Argumento 2 e 3 de entrada deve ter valores de 0 a 27"
	else:
		print "Enter the correct number of arguments!!"
