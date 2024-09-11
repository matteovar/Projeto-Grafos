class TGrafoND:
    TAM_MAX_DEFAULT = 100
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n 
        self.m = 0
        self.adj = [[0.0 for _ in range(n)] for _ in range(n)]  

    def insereA(self, v, w, peso=1.0):
        if self.adj[v][w] == 0.0 and self.adj[w][v] == 0.0:
            self.adj[v][w] = peso
            self.adj[w][v] = peso
            self.m += 1 
        else:
            print("Aresta ja existe")

    def insereV(self):
        self.n += 1
        nova_linha = [0.0] * self.n
        self.adj.append(nova_linha)

        for i in range(self.n - 1):
            self.adj[i].append(0.0)  

    def removeA(self, v, w):
        if self.adj[v][w] != 0.0 and self.adj[w][v] != 0.0:
            self.adj[v][w] = 0.0
            self.adj[w][v] = 0.0
            self.m -= 1

    def removeV(self, v):
        for i in range(self.n):
            if self.adj[v][i] != 0.0 and self.adj[i][v]!=0.0: 
                self.removeA(v, i)

        self.adj.pop(v)

        for i in range(len(self.adj)):
            self.adj[i].pop(v)
        self.n -= 1

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

    def verificarDirecionado(self):
            for i in range(self.n):
                for j in range( self.n):
                    if self.adj[i][j] != self.adj[j][i]:
                        return True  
            return False 
    
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0.0:
                    print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]:.2f} ", end="")
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0.00 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0.0:
                    print(f"{self.adj[i][w]:.2f} ", end="")
                else:
                    print("0.00 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

    def carregarDoArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            tipo_grafo = int(linhas[0].strip())
            num_vertices = int(linhas[1].strip())
            vertices = []
            for i in range(2, 2 + num_vertices):
                _, indice = linhas[i].strip().rsplit(maxsplit=1)
                vertices.append(int(indice))
            num_arestas_index = 2 + num_vertices
            num_arestas = int(linhas[num_arestas_index].strip())
            self.n = num_vertices
            self.adj = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
            self.m = 0 
            for i in range(num_arestas_index + 1, num_arestas_index + 1 + num_arestas):
                v, w, peso = map(int, linhas[i].strip().split())
                self.insereA(v, w, peso)
            


    def carregarDoArquivo2(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())

    def salvarEmArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"2\n")
            arquivo.write(f"{self.n}\n")
            for i in range(self.n):
                arquivo.write(f"{i}\n")
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