def consultar_estoque(produto_id, produtos=None):
    if produtos is None:
        produtos = {}

    '''consulta o estoque de um produto específico'''
    if produto_id in produtos:
        produto = produtos[produto_id]
        print('\n====Dados do produto====')
        print(f'ID: {produto_id}')
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
    else:
        print('\nProduto não encontrado!')


