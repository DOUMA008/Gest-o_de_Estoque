produtos = {}

proximo_id = 1

def cadastrar_produto(nome, categoria, preco, quantidade, estoque=None):
    """Registra novo produto no sistema"""

    global proximo_id

    if estoque is None:
        estoque = produtos

    estoque[proximo_id] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"\nProduto cadastrado com sucesso!")
    print(f"ID do produto: {proximo_id}")

    proximo_id += 1
