from app.banco import cursor

def alertar_estoque_baixo():
    try:
        limite = int(input('digite quantidade limite para alertar estoque baixo: '))
    except ValueError:
        print('apenas números inteiros são válidos!')
        return

    sql = '''select id, nome , quantidade 
    from produtos
    where quantidade < %s'''

    cursor.execute(sql,(limite,))
    produtos = cursor.fetchall()

    if not produtos:
        print('nenhum produto cadastrado!')
        return

    print('\n===ALERTAR ESTOQUE BAIXO===')

    for produto in produtos :
        print(
           f'ID: {produto[0]} | ' 
           f'Produto: {produto[1]} | '
           f'Quantidade: {produto[2]}'
        )
        