def registrar_saida(produto_id, quantidade, produtos=None):
    if produtos is None:
        produtos = {}

    """Registra a saida de um produto do estoque."""
    if produto_id in produtos:
        estoque_atual = produtos[produto_id]["quantidade"]
        if estoque_atual >= quantidade:
            produtos[produto_id]["quantidade"] -= quantidade
            print(f'\nSaida registrada com sucesso! Novo estoque: {produtos[produto_id]["quantidade"]}')
        else:
            print("\nQuantidade insuficiente em estoque!")
    else:
        print("\nProduto nao encontrado!")
