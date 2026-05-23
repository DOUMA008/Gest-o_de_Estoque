def registrar_entrada(produto_id, quantidade, produtos=None):
    if produtos is None:
        produtos = {}

    """Registra a entrada de um produto no estoque"""
    if produto_id in produtos:
        produtos[produto_id]['quantidade'] += quantidade
        print(f'\nEntrada registrada com sucesso! Novo estoque: {produtos[produto_id]["quantidade"]}')
    else:
        print('\nProduto não encontrado!')
