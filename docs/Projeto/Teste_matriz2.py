import sys
from Grafos_Matriz import TGrafoND  # type: ignore

g = None
def menu():
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Carregar grafo de arquivo")
        print("2. Gravar dados no arquivo de saída (e exibir grafo)")
        print("3. Mostrar conteudo grafo")
        print("4. Inserir vertice")
        print("5. Inserir aresta")
        print("6. Remover vertice")
        print("7. Remover aresta")
        print("8. Verificar conexividades")
        print("8. Sair")
        print("-----------------------")
        opcao = input("Escolha uma opção: ")


        if opcao == '1':
            arquivo = input("Digite o nome do arquivo de entrada: ")
            g = TGrafoND(0)
            g.carregarDoArquivo(arquivo)
            print("Grafo carregado com sucesso!")

        elif opcao == '2':
            if g:
                nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
                g.salvarEmArquivo(nome_arquivo_saida)
            else:
                print("nao foi, se fudeo")

        elif opcao == '3':
            if g:
                print("Grafo")
                g.show()
            else:
                print("Nao tem grafo")
        
        elif opcao == '4':
            print("Nome do aeroporto desejado: ")
            nome = input("Nome: ")
            g.insereV(nome)
            g.salvarEmArquivo(nome_arquivo_saida)
            g.show()
    
        elif opcao == '5':
            print("Valores das arestas e do peso:")
            valor_1 = int(input("Aresta 1:"))
            valor_2 = int(input("Aresta 2: "))
            peso_inserir = int(input("Peso da aresta: "))
            g.insereA(valor_1,valor_2,peso_inserir)
            g.salvarEmArquivo(nome_arquivo_saida)
            g.show()
        
        elif opcao == '6':
            remover = int(input("Valor que deseja remover: "))
            g.removeV(remover)
            g.salvarEmArquivo(nome_arquivo_saida)
            g.show()

        elif opcao == '7':
            remover_1 = int(input("Remover vertice 1: "))
            remover_2 = int(input("Remover vertice 2: "))
            g.removeA(remover_1,remover_2)
            g.salvarEmArquivo(nome_arquivo_saida)
            g.show()
        elif opcao == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
