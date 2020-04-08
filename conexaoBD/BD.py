import pymysql.cursors

def conectar():
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='SOFIA',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conexao
    except:
        print('Erro ao conectar ao Banco de Dados')

def select(conexao, argumento):
    try:
        with conexao.cursor() as cursor:
            cursor.execute(f'select * from {argumento}')
            resultado = cursor.fetchall()
            return resultado
    except:
        print('Erro Select')