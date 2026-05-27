def alerta_estoque_baixo(produtos=None, limite=None):   # Função responsável por identificar produtos com estoque baixo
    if produtos is None:    # Caso nenhum dicionário seja informado, cria um vazio
        produtos = {}
    if limite is None:    # Caso nenhum limite seja informado, define como 0
        limite = 0

    """Exibe um alerta para produtos com estoque baixo."""
    print("\n==== Alerta de Estoque Baixo ====")    # Exibe o título da seção
    encontrou = False    # Variável para verificar se encontrou produtos críticos

    for produto_id, produto in produtos.items():    # Percorre todos os produtos cadastrados
        if produto["quantidade"] < limite:   # Verifica se a quantidade é menor que o limite informado
            encontrou = True   # Marca que encontrou produto com estoque baixo
            print(f'ID: {produto_id} - Nome: {produto["nome"]} - Quantidade: {produto["quantidade"]}')   # Exibe os dados do produto

    if not encontrou:    # Caso nenhum produto tenha estoque baixo
        print("Nenhum produto com estoque baixo!")
