# Dicionário que armazena todos os produtos cadastrados
produtos = {}

# Variável responsável por gerar IDs únicos para os produtos
proximo_id = 1

# Função responsável por cadastrar novos produtos no estoque
def cadastrar_produto(nome, categoria, preco, quantidade, estoque=None):
    """Registra novo produto no sistema"""

    # Permite alterar a variável global proximo_id
    global proximo_id

    # Caso nenhum estoque seja informado, usa o dicionário principal
    if estoque is None:
        estoque = produtos

     # Adiciona o produto ao dicionário usando o ID atual
    estoque[proximo_id] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"\nProduto cadastrado com sucesso!")   # Exibe mensagem de sucesso
    print(f"ID do produto: {proximo_id}")   # Mostra o ID gerado para o produto

    proximo_id += 1       # Incrementa o ID para o próximo cadastro
