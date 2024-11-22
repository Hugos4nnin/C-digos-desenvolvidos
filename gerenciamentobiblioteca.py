import matplotlib.pyplot as plt
class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao

  def __str__(self):
    return f"{self.titulo}por {self.autor}, Publicado em {self.ano_publicacao}"

biblioteca = []
anos = []
def adicionar_livro(titulo, autor, ano_publicacao):
  novo_livro = Livro(titulo, autor, ano_publicacao)
  biblioteca.append(novo_livro)
  anos.append(ano_publicacao)
  print(f"O livro '{titulo}' foi adicionado à  biblioteca.")

def listar_livros():
  print("Livros na Biblioteca: ")
  for livro in biblioteca:
    print(livro)

adicionar_livro("Dom quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
adicionar_livro("As aventuras de Guga", "Huguinho", 1940)
adicionar_livro("Em busca do Ovo perdido", "Guga", 2024)
adicionar_livro("Solidão e Solitude", "Hugo", 2003)

listar_livros()
anos = list(set(anos))
anos.sort()
contagem_por_ano = [anos.count(ano) for ano in anos]

plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por ano de publicação')

for i, valor in enumerate(contagem_por_ano):
  plt.text(anos[i], valor, str(valor), ha='center', va='bottom')
plt.grid(True)
plt.show()
