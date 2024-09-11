from Grafos_Matriz import TGrafoND # type: ignore

# Instancia o grafo
g = TGrafoND()

# Carrega o grafo a partir de um arquivo
g.carregarDoArquivo('ordem_das_cidades.txt')

# Mostra o grafo carregado
print("\nGrafo original:")
g.salvarEmArquivo('grafo_modificado.txt')
g.carregarDoArquivo2('grafo_modificado.txt')
g.show()
# Remove o vértice 7
print("\nGrafo após remover o vértice:")
g.removeV(7)

g.salvarEmArquivo('grafo_modificado.txt')
g.carregarDoArquivo2('grafo_modificado.txt')
g.show()

g.insereV(7)
g.salvarEmArquivo('grafo_modificado.txt')
g.carregarDoArquivo2('grafo_modificado.txt')
g.show()

g.insereA(50,32,1879)
g.salvarEmArquivo('grafo_modificado.txt')
g.carregarDoArquivo2('grafo_modificado.txt')
g.show()
