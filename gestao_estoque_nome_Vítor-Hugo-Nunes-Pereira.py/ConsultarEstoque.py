def consultar_estoque(produto_id, produtos=None):
    if produtos is None:
        produtos = {}

    """Consulta o estoque de um produto especifico."""
    if produto_id in produtos:
        produto = produtos[produto_id]
        print("\n==== Dados do produto ====")
        print(f"ID: {produto_id}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preco: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
    else:
        print("\nProduto nao encontrado!")
