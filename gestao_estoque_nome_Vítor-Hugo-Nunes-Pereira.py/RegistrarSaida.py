def registrar_saida(produto_id, quantidade, produtos=None):   # Função responsável por registrar a saída de produtos do estoque
    if produtos is None:   # Caso nenhum dicionário seja informado, cria um vazio
        produtos = {}

    """Registra a saida de um produto do estoque."""
    if produto_id in produtos:    # Verifica se o produto existe no dicionário
        estoque_atual = produtos[produto_id]["quantidade"]    # Armazena a quantidade atual do produto
        if estoque_atual >= quantidade:    # Verifica se há quantidade suficiente no estoque
            produtos[produto_id]["quantidade"] -= quantidade   # Remove a quantidade informada do estoque
            print(f'\nSaida registrada com sucesso! Novo estoque: {produtos[produto_id]["quantidade"]}')    # Exibe mensagem de sucesso com o novo estoque
        else:
            print("\nQuantidade insuficiente em estoque!")   # Mensagem exibida caso não tenha estoque suficiente
    else:
        print("\nProduto nao encontrado!")    # Mensagem exibida caso o produto não exista
