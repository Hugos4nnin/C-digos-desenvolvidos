from datetime import datetime
from typing import List

# Classe Categoria para organizar os produtos
class Categoria:
    def __init__(self, nome: str, descricao: str = ""):
        self.nome = nome
        self.descricao = descricao

# Classe Produto para representar cada item do estoque
class Produto:
    def __init__(self, codigo: str, nome: str, categoria: Categoria, preco: float, quantidade: int = 0):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_quantidade(self, quantidade: int):
        self.quantidade += quantidade

# Classe Movimentação para registrar entradas e saídas de estoque
class Movimentacao:
    def __init__(self, produto: Produto, quantidade: int, tipo: str):
        self.produto = produto
        self.quantidade = quantidade
        self.tipo = tipo  # "entrada" ou "saida"
        self.data = datetime.now()

# Banco de dados simulado para armazenar produtos e categorias
produtos = []
categorias = []

# Função para cadastrar uma nova categoria
def cadastrar_categoria(nome: str, descricao: str = ""):
    categoria = Categoria(nome, descricao)
    categorias.append(categoria)
    return categoria

# Função para cadastrar um novo produto
def cadastrar_produto(codigo: str, nome: str, categoria: Categoria, preco: float, quantidade: int = 0):
    produto = Produto(codigo, nome, categoria, preco, quantidade)
    produtos.append(produto)
    return produto

# Função para consultar um produto pelo código
def consultar_produto_por_codigo(codigo: str) -> Produto:
    for produto in produtos:
        if produto.codigo == codigo:
            return produto
    return None

# Função para listar todos os produtos de uma categoria
def listar_produtos_por_categoria(categoria: Categoria) -> List[Produto]:
    return [produto for produto in produtos if produto.categoria == categoria]

# Banco de dados simulado para armazenar movimentações
movimentacoes = []

# Função para registrar uma movimentação (entrada ou saída)
def registrar_movimentacao(codigo_produto: str, quantidade: int, tipo: str):
    produto = consultar_produto_por_codigo(codigo_produto)
    if not produto:
        print("Produto não encontrado.")
        return None

    # Determina se é entrada ou saída
    if tipo == "entrada":
        produto.atualizar_quantidade(quantidade)
    elif tipo == "saida":
        if produto.quantidade >= quantidade:
            produto.atualizar_quantidade(-quantidade)
        else:
            print("Quantidade insuficiente em estoque.")
            return None

    # Registra a movimentação
    movimentacao = Movimentacao(produto, quantidade, tipo)
    movimentacoes.append(movimentacao)
    return movimentacao

# Função para gerar relatório de estoque
def gerar_relatorio_estoque():
    print("Relatório de Estoque:")
    for produto in produtos:
        print(f"Código: {produto.codigo} | Nome: {produto.nome} | Quantidade: {produto.quantidade}")

# Função para consultar o histórico de movimentações de um produto
def consultar_historico_movimentacoes(codigo_produto: str):
    produto = consultar_produto_por_codigo(codigo_produto)
    if not produto:
        print("Produto não encontrado.")
        return []

    # Filtra movimentações do produto
    historico = [mov for mov in movimentacoes if mov.produto == produto]

    print(f"Histórico de Movimentações para {produto.nome}:")
    for mov in historico:
        print(f"{mov.data} - {mov.tipo.capitalize()} - Quantidade: {mov.quantidade}")
    return historico

# Cadastro de categoria e produto
categoria = cadastrar_categoria("Periféricos")
produto = cadastrar_produto("003", "Teclado Mecânico RGB", categoria, 250.0, 20)

# Consulta do produto cadastrado
consultar_produto_por_codigo("003")
produto = consultar_produto_por_codigo("003")
if produto:
    print(f"Código: {produto.codigo} | Nome: {produto.nome} | Categoria: {produto.categoria.nome} | Preço: R${produto.preco} | Quantidade: {produto.quantidade}")


# Movimentações de entrada e saída

registrar_movimentacao("003", 5, "entrada")
registrar_movimentacao("003", 4, "saida")
print(f"Código: {produto.codigo} | Nome: {produto.nome} | Quantidade Atualizada: {produto.quantidade}")

# Gerar relatório de estoque
gerar_relatorio_estoque()

# Consultar histórico de movimentações
consultar_historico_movimentacoes("003")
