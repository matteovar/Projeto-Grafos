import sys
from Grafos_Matriz import TGrafoND  # type: ignore

g = TGrafoND()
def menu():
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Ler dados do arquivo de entrada")
        print("2. Gravar dados no arquivo de saída")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar conteúdo do arquivo")
        print("8. Mostrar grafo")
        print("9. Verificar conexividade do grafo")
        print("10. Coloracao")
        print("11. Dijkstra")
        print("12. Caminho Euleriano")
        print("13. Caminho Hamiltoniano")
        print("14. Encerrar a aplicação")
        print("-----------------------")
        opcao = input("Escolha uma opção: ")
        print("\n")


        if opcao == '1':
            arquivo = input("Digite o nome do arquivo de entrada: ")
            g = TGrafoND(0)
            g.carregarDoArquivo(arquivo)
            print("Agora carregue o arquivo de saida, que ira salvar o grafo")

        elif opcao == '2':
            if g:
                nome_arquivo_saida = input("Carregue o arquivo de saida: ")
                g.salvarEmArquivo(nome_arquivo_saida)
            else:
                print("nao tem") 

        elif opcao == '3':
            if g:
                print("Nome do aeroporto desejado: ")
                nome = input("Nome: ")
                g.insereV(nome)
                g.salvarEmArquivo(nome_arquivo_saida)

            else:
                print("Nao existe")
    
        elif opcao == '4':
            if g:
                print("Valores(vertices) das arestas e valor do peso:")
                valor_1 = int(input("Vertice 1:"))
                valor_2 = int(input("Vertice 2: "))
                peso_inserir = int(input("Peso da aresta: "))
                g.insereA(valor_1,valor_2,peso_inserir)
                g.salvarEmArquivo(nome_arquivo_saida)
            else:
                print("Nao existe")

        elif opcao == '5':
            remover = int(input("Valor(vertice) que deseja remover: "))
            g.removeV(remover)
            g.salvarEmArquivo(nome_arquivo_saida)

        elif opcao == '6':
            if g:
                remover_1 = int(input("Remover vertice 1: "))
                remover_2 = int(input("Remover vertice 2: "))
                g.removeA(remover_1,remover_2)
                g.salvarEmArquivo(nome_arquivo_saida)

            else:
                print("Nao tem")

        elif opcao == '7':
            if g:
                print("Conteudo do arquivo:")
                g.show(nome_arquivo_saida)
            else:
                print("Arquivo não existe.")

        elif opcao == '8':
            if g:
                print("Grafo:")
                g.mostrarGrafo()
            else:
                print("Grafo não existe.")

        elif opcao == '9':
            if g.isConexo():
                print("Grafo conexo\n")
            else:
                print("Grafo nao conexo\n")
        
        elif opcao == '10':
            g.coloracao()

        elif opcao =='11':
            g.mostrarCaminhoMinimo()


        elif opcao == '12':
            tem_caminho_euleriano, vertices_impares = g.temCaminhoEuleriano()
            if tem_caminho_euleriano:
                print("O grafo tem um caminho euleriano.")
                print(f"Vértices com grau ímpar: {vertices_impares}")
            else:
                print("O grafo não tem um caminho euleriano.")

        elif opcao == '13':
            tem_caminho_hamiltoniano, caminho_hamiltoniano = g.temCaminhoHamiltoniano()
            if tem_caminho_hamiltoniano:
                print("O grafo tem um caminho hamiltoniano.")
            else:
                print("O grafo não tem um caminho hamiltoniano.")

        elif opcao == '14':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()