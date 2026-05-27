def registrar_entrada(produto_id, quantidade, produtos=None):   # Função responsável por registrar a entrada de produtos no estoque
    if produtos is None:   # Caso nenhum dicionário seja informado, cria um vazio
        produtos = {}

    """Registra a entrada de um produto no estoque."""
    if produto_id in produtos:    # Verifica se o produto existe no dicionário
        produtos[produto_id]["quantidade"] += quantidade    # Adiciona a quantidade informada ao estoque atual
        print(f'\nEntrada registrada com sucesso! Novo estoque: {produtos[produto_id]["quantidade"]}')   # Exibe mensagem de sucesso com o novo estoque
    else:   
        print("\nProduto nao encontrado!")   # Mensagem exibida caso o produto não exista
