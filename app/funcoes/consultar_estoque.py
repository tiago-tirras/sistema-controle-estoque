from app.banco import cursor,conexao 

def consultar_estoque():


    sql = 'select id,nome,categoria,preco , quantiadade from produto'

    cursor.execute(sql)

    produtos = cursor.fetchall()

    if not produtos :
        print('estoque vazio!')
        return

    print('\n===ESTOQUE ATUAL===')

    for produto in produtos:

        preco_total = produto[3] * produto[4]

        print(
            f'\nID: {produto[0]}'
            f'\nProduto: {produto[1]}'
            f'\nCategoria: {produto[2]}'
            f'\nPreço: {produto[3]}'
            f'\nQuantidade: {produto[4]}'
            f'\nPreço total: R$ {preco_total:.2f}'
            )