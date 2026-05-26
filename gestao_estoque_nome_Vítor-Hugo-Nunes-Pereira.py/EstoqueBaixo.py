def alerta_estoque_baixo(produtos=None, limite=None):
    if produtos is None:
        produtos = {}
    if limite is None:
        limite = 0

    """Exibe um alerta para produtos com estoque baixo."""
    print("\n==== Alerta de Estoque Baixo ====")
    encontrou = False

    for produto_id, produto in produtos.items():
        if produto["quantidade"] < limite:
            encontrou = True
            print(f'ID: {produto_id} - Nome: {produto["nome"]} - Quantidade: {produto["quantidade"]}')

    if not encontrou:
        print("Nenhum produto com estoque baixo!")
