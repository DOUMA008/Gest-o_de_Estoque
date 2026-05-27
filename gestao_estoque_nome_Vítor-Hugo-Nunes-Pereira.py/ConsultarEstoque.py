def consultar_estoque(produto_id, produtos=None):   # Função responsável por consultar os dados e estoque de um produto
    if produtos is None:   # Caso nenhum dicionário seja informado, cria um vazio

        produtos = {}

    """Consulta o estoque de um produto especifico."""
    if produto_id in produtos:    # Verifica se o ID do produto existe no dicionário
        produto = produtos[produto_id]   # Armazena os dados do produto em uma variável
        print("\n==== Dados do produto ====")    # Exibe as informações do produto
        print(f"ID: {produto_id}")    # Mostra o ID do produto
        print(f"Nome: {produto['nome']}")   # Mostra o nome do produto
        print(f"Categoria: {produto['categoria']}")   # Mostra a categoria do produto
        print(f"Preco: R$ {produto['preco']:.2f}")  # Mostra o preço formatado com duas casas decimais
        print(f"Quantidade: {produto['quantidade']}")  # Mostra a quantidade disponível em estoque
    else:
        print("\nProduto nao encontrado!")  # Mensagem exibida caso o produto não exista
