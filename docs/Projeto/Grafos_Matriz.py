class TGrafoND:
    TAM_MAX_DEFAULT = 1000
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n 
        self.m = 0
        self.adj = [[0.0 for _ in range(n)] for _ in range(n)]  

    def insereA(self, v, w, peso=1.0):
        if v >= self.n or w >= self.n:
            print("Um ou ambos os vértices não existem.")
            return  # Retorna ao menu
        if self.adj[v][w] == 0.0 and self.adj[w][v] == 0.0:
            self.adj[v][w] = peso
            self.adj[w][v] = peso
            self.m += 1
        else:
            print("Aresta já existe.")


    def insereV(self, nome_vertice):
        self.n += 1
        self.nomes_vertices.append(nome_vertice)  # Adiciona o nome do novo vértice
        nova_linha = [0.0] * self.n
        self.adj.append(nova_linha)

        for i in range(self.n - 1):
            self.adj[i].append(0.0)   

    def removeA(self, v, w):
        if v >= self.n or w >= self.n:
            print("Um ou ambos os vértices não existem.")
            return  # Retorna ao menu
        if self.adj[v][w] != 0.0 and self.adj[w][v] != 0.0:
            self.adj[v][w] = 0.0
            self.adj[w][v] = 0.0
            self.m -= 1
        else:
            print("Aresta não existe.")

    def removeV(self, v):
        if v >= self.n:
            print("Vértice inválido!")
            return

        # Remover todas as arestas conectadas ao vértice v
        for i in range(self.n):
            if self.adj[v][i] != 0.0:  # Verifica se existe aresta entre v e i
                self.removeA(v, i)  # Remove a aresta v <-> i

        # Remove o vértice da matriz de adjacência
        self.adj.pop(v)  # Remove a linha correspondente ao vértice v
        for i in range(len(self.adj)):
            self.adj[i].pop(v)  # Remove a coluna correspondente ao vértice v

        # Remove o nome do vértice da lista de nomes
        self.nomes_vertices.pop(v)

        # Atualiza o número de vértices
        self.n -= 1

        print(f"Vértice {v} removido com sucesso.")
    
    def dfs(self, v, visitados):
        visitados[v] = True  
        for i in range(self.n):
            if self.adj[v][i] != 0.0 and not visitados[i]:  
                self.dfs(i, visitados)

    def isConexo(self):
        visitados = [False] * self.n 

        start_vertex = -1
        for i in range(self.n):
            if any(self.adj[i][j] != 0.0 for j in range(self.n)):
                start_vertex = i
                break

        if start_vertex == -1:
            print("Grafo vazio ou sem arestas.")
            return True

        self.dfs(start_vertex, visitados)

        for i in range(self.n):
            if not visitados[i] and any(self.adj[i][j] != 0.0 for j in range(self.n)):
                return False 

        return True
    def show(self,nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())
        

    def carregarDoArquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                tipo_grafo = int(linhas[0].strip())
                num_vertices = int(linhas[1].strip())
                self.nomes_vertices = []
                for i in range(2, 2 + num_vertices):
                    descricao, indice = linhas[i].strip().rsplit(maxsplit=1)
                    self.nomes_vertices.append(descricao)

                num_arestas_index = 2 + num_vertices
                num_arestas = int(linhas[num_arestas_index].strip())
                self.n = num_vertices
                self.adj = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
                self.m = 0
                for i in range(num_arestas_index + 1, num_arestas_index + 1 + num_arestas):
                    v, w, peso = map(int, linhas[i].strip().split())
                    self.insereA(v, w, peso)
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não foi encontrado.")



    def salvarEmArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"2\n{self.n}\n")
            for i in range(self.n):
                arquivo.write(f"{self.nomes_vertices[i]} {i}\n")
            num_arestas = 0
            for i in range(self.n):
                for j in range(i+1, self.n):
                    if self.adj[i][j] != 0.0:
                        num_arestas += 1
            arquivo.write(f"{num_arestas}\n")

            for i in range(self.n):
                for j in range(i+1, self.n):
                    if self.adj[i][j] != 0.0:
                        arquivo.write(f"{i} {j} {int(self.adj[i][j])}\n")
            
            for i in range(self.n):
                linha = [f"{peso if peso is not None else '∞'}" for peso in self.adj[i]]
                arquivo.write(f"Matriz {i}: {linha}\n")
