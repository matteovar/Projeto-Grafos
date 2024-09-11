import sys

from Grafos_Matriz import TGrafoND # type: ignore

# Abra o arquivo em modo de escrita
with open('docs/output.txt', 'w') as f:
    # Redirecione a saída padrão para o arquivo
    sys.stdout = f
    
    g = TGrafoND()

    # Carrega o grafo a partir de um arquivo
    g.carregarDoArquivo('docs/projeto/ordem_das_cidades.txt')

    # Mostra o grafo carregado
    print("\nGrafo original:")
    g.salvarEmArquivo('docs/projeto/grafo_modificado.txt')
    g.carregarDoArquivo2('docs/projeto/grafo_modificado.txt')
    g.show()
    # Remove o vértice 7
    n = 7
    print(f"\nGrafo apos remover o vertice:{n}")
   
    g.removeV(n)

    g.salvarEmArquivo('docs/projeto/grafo_modificado.txt')
    g.carregarDoArquivo2('docs/projeto/grafo_modificado.txt')
    g.show()

    print("\nGrafo apos inserir um vertice")
    g.insereV()
    g.salvarEmArquivo('docs/projeto/grafo_modificado.txt')
    g.carregarDoArquivo2('docs/projeto/grafo_modificado.txt')
    g.show()

    n1 = 50
    n2 = 31
    peso1 = 1879
    print(f"\nGrafo apos inserir aresta {n1} {n2} e com peso {peso1}")
    
    g.insereA(n1,n2,peso1)
    g.salvarEmArquivo('docs/projeto/grafo_modificado.txt')
    g.carregarDoArquivo2('docs/projeto/grafo_modificado.txt')
    g.show()


    # Restaure a saída padrão para o console
    sys.stdout = sys.__stdout__


