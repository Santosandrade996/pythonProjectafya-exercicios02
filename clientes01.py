from future import annotations
import time as t
import pyodbc as p
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

server = 'LOCALHOST\SQLEXPRESS'
database = 'loja'
cnx = p.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_connection=yes;')
cursor = cnx.cursor()

def listar_clientes():
    clientes = '''
        SELECT * FROM cliente_loja
    '''
    cursor.execute(clientes)
    for linha in cursor.fetchall():
        print(linha)

def listar_motocicletas():
    motocicletas = '''
        SELECT * FROM motocicleta_loja
    '''
    cursor.execute(motocicletas)
    for linha in cursor.fetchall():
        print(linha)

def listar_vendas():
    vendas = '''
        SELECT venda.id_venda, cliente_loja.nome, motocicleta_loja.marca, motocicleta_loja.modelo, venda.valor
        FROM venda
        INNER JOIN cliente_loja ON venda.id_cliente = cliente_loja.id_cliente
        INNER JOIN motocicleta_loja ON venda.id_motocicleta = motocicleta_loja.id_motocicleta
    '''
    cursor.execute(vendas)
    for linha in cursor.fetchall():
        print(linha)

def consultar_venda():
    listar_vendas()
    id_venda = int(input('Digite o ID da Venda que deseja consultar: '))
    consulta = '''
        SELECT venda.id_venda, cliente_loja.nome, motocicleta_loja.marca, motocicleta_loja.modelo, venda.valor
        FROM venda
        INNER JOIN cliente_loja ON venda.id_cliente = cliente_loja.id_cliente
        INNER JOIN motocicleta_loja ON venda.id_motocicleta = motocicleta_loja.id_motocicleta
        WHERE venda.id_venda = {}
    '''.format(id_venda)
    cursor.execute(consulta)
    venda = cursor.fetchone()
    if venda:
        print('ID Venda:', venda[0])
        print('Cliente:', venda[1])
        print('Motocicleta:', venda[2], venda[3])
        print('Valor:', venda[4])
    else:
        print('Venda não encontrada.')

def cadastrar_cliente():
    print('-' * 25, 'CADASTRO CLIENTE', '-' * 25)
    nome = str(input('Digite o Nome do Cliente: '))
    sobrenome = str(input('Digite o Sobrenome do Cliente: '))
    cep = str(input('Digite o CEP do Cliente: '))
    inserir = '''
        INSERT INTO cliente_loja (nome, sobrenome, cep) VALUES ('{}', '{}', '{}')
    '''.format(nome, sobrenome, cep)
    cursor.execute(inserir)
    cursor.commit()
    print('Cliente cadastrado!')
    t.sleep(2)

def alterar_cliente():
    listar_clientes()
    id_cliente = int(input('Digite o ID do Cliente que deseja alterar: '))

    consulta = '''
        SELECT * FROM cliente_loja WHERE id_cliente = {}
    '''.format(id_cliente)
    cursor.execute(consulta)
    cliente = cursor.fetchone()

    if cliente:
        print('Dados atuais do cliente:')
        print('ID Cliente:', cliente[0])
        print('Nome:', cliente[1])
        print('Sobrenome:', cliente[2])
        print('CEP:', cliente[3])

        nome = str(input('Digite o novo Nome do Cliente: '))
        sobrenome = str(input('Digite o novo Sobrenome do Cliente: '))
        cep = str(input('Digite o novo CEP do Cliente: '))

        atualizar = '''
            UPDATE cliente_loja
            SET nome = '{}', sobrenome = '{}', cep = '{}'
            WHERE id_cliente = {}
        '''.format(nome, sobrenome, cep, id_cliente)

        cursor.execute(atualizar)
        cursor.commit()
        print('Cliente alterado com sucesso!')
    else:
        print('Cliente não encontrado.')

    t.sleep(2)


def alterar_motocicleta():
    listar_motocicletas()
    id_motocicleta = int(input('Digite o ID da Motocicleta que deseja alterar: '))

    consulta = '''
        SELECT * FROM motocicleta_loja WHERE id_motocicleta = {}
    '''.format(id_motocicleta)
    cursor.execute(consulta)
    motocicleta = cursor.fetchone()
    f
    motocicleta:
    print('Dados atuais da motocicleta:')
    print('ID Motocicleta:', motocicleta[0])
    print('Marca:', motocicleta[1])
    print('Modelo:', motocicleta[2])
    print('Ano:', motocicleta[3])
    Giselle
    Santos, [05 / 06 / 2023 13: 28]
    marca = str(input('Digite a nova Marca da Motocicleta: '))
    modelo = str(input('Digite o novo Modelo da Motocicleta: '))
    ano = int(input('Digite o novo Ano da Motocicleta: '))

    atualizar = '''
                        UPDATE motocicleta_loja
                        SET marca = '{}', modelo = '{}', ano = {}
                        WHERE id_motocicleta = {}
                    '''.format(marca, modelo, ano, id_motocicleta)

    cursor.execute(atualizar)
    cursor.commit()
    print('Motocicleta alterada com sucesso!')

else:
print('Motocicleta não encontrada.')

t.sleep(2)


def excluir_cliente():
    listar_clientes()
    id_cliente = int(input('Digite o ID do Cliente que deseja excluir: '))

    confirmacao = input('Tem certeza que deseja excluir o cliente? (S/N): ')

    if confirmacao.lower() == 's':
        delete_cliente = '''
                        DELETE FROM cliente_loja WHERE id_cliente = {}
                    '''.format(id_cliente)
        cursor.execute(delete_cliente)
        cursor.commit()
        print('Cliente excluído com sucesso!')
    else:
        print('Operação cancelada.')

    t.sleep(2)


def cadastrar_motocicleta():
    print('-' * 25, 'CADASTRO MOTOCICLETA', '-' * 25)
    marca = str(input('Digite a Marca da Motocicleta: '))
    modelo = str(input('Digite o Modelo da Motocicleta: '))
    ano = int(input('Digite o Ano da Motocicleta: '))
    inserir = '''
                    INSERT INTO motocicleta_loja (marca, modelo, ano) VALUES ('{}', '{}', {})
                '''.format(marca, modelo, ano)
    cursor.execute(inserir)
    cursor.commit()
    print('Motocicleta cadastrada!')
    t.sleep(2)


def excluir_motocicleta():
    listar_motocicletas()
    id_motocicleta = int(input('Digite o ID da Motocicleta que deseja excluir: '))

    confirmacao = input('Tem certeza que deseja excluir a motocicleta? (S/N): ')

    if confirmacao.lower() == 's':
        delete_motocicleta = '''
                        DELETE FROM motocicleta_loja WHERE id_motocicleta = {}
                    '''.format(id_motocicleta)
        cursor.execute(delete_motocicleta)
        cursor.commit()
        print('Motocicleta excluída com sucesso!')
    else:
        print('Operação cancelada.')

    t.sleep(2)


def cadastrar_venda():
    clear_screen()
    print('-' * 25, 'VENDA DE MOTOCICLETA', '-' * 25)
    listar_clientes()
    id_cliente = int(input('Digite o ID do Cliente: '))
    listar_motocicletas()
    id_motocicleta = int(input('Digite o ID da Motocicleta: '))
    valor = float(input('Digite o valor da venda: '))

    inserir_venda = '''
                    INSERT INTO venda (id_cliente, id_motocicleta, valor) VALUES ({}, {}, {})
                '''.format(id_cliente, id_motocicleta, valor)
    cursor.execute(inserir_venda)
    cursor.commit()

    clear_screen()
    print('Venda realizada!')
    t.sleep(2)


def excluir_venda():
    listar_vendas()
    id_venda = int(input('Digite o ID da Venda que deseja excluir: '))

    confirmacao = input('Tem certeza que deseja excluir a venda? (S/N): ')

    if confirmacao.lower() == 's':
        delete_venda = '''
                        DELETE FROM venda WHERE id_venda = {}
                    '''.format(id_venda)
        cursor.execute(delete_venda)
        cursor.commit()
        print('Venda excluída com sucesso!')
    else:
        print('Operação cancelada.')

    t.sleep(2)

    def exibir_menu():
        print('-' * 25, 'MENU PRINCIPAL', '-' * 25)
        print('1. Clientes')
        print('2. Motocicletas')
        print('3. Vendas')
        print('4. Sair')

    def exibir_menu_clientes():
        print('-' * 25, 'MENU CLIENTES', '-' * 25)
        print('1. Cadastrar Cliente')
        print('2. Listar Clientes')
        print('3. Alterar Cliente')
        print('4. Excluir Cliente')
        print('5. Voltar')

    def exibir_menu_motocicletas():
        print('-' * 25, 'MENU MOTOCICLETAS', '-' * 25)
        print('1. Cadastrar Motocicleta')
        print('2. Listar Motocicletas')
        print('3. Alterar Motocicleta')
        print('4. Excluir Motocicleta')
        print('5. Voltar')

    Giselle
    Santos, [05 / 06 / 2023 13: 28]

    def exibir_menu_vendas():
        print('-' * 25, 'MENU VENDAS', '-' * 25)
        print('1. Cadastrar Venda')
        print('2. Listar Vendas')
        print('3. Consultar Venda')
        print('4. Excluir Venda')
        print('5. Voltar')

    def main():
        while True:
            clear_screen()
            exibir_menu()
            opcao = input('Digite a opção desejada: ')

            if opcao == '1':
                while True:
                    clear_screen()
                    exibir_menu_clientes()
                    opcao_clientes = input('Digite a opção desejada: ')

                    if opcao_clientes == '1':
                        cadastrar_cliente()
                    elif opcao_clientes == '2':
                        clear_screen()
                        listar_clientes()
                        t.sleep(5)
                    elif opcao_clientes == '3':
                        alterar_cliente()
                    elif opcao_clientes == '4':
                        excluir_cliente()
                    elif opcao_clientes == '5':
                        break
                    else:
                        print('Opção inválida!')

            elif opcao == '2':
                while True:
                    clear_screen()
                    exibir_menu_motocicletas()
                    opcao_motocicletas = input('Digite a opção desejada: ')

                    if opcao_motocicletas == '1':
                        cadastrar_motocicleta()
                    elif opcao_motocicletas == '2':
                        clear_screen()
                        listar_motocicletas()
                        t.sleep(5)
                    elif opcao_motocicletas == '3':
                        alterar_motocicleta()
                    elif opcao_motocicletas == '4':
                        excluir_motocicleta()
                    elif opcao_motocicletas == '5':
                        break
                    else:
                        print('Opção inválida!')

            elif opcao == '3':
                while True:
                    clear_screen()
                    exibir_menu_vendas()
                    opcao_vendas = input('Digite a opção desejada: ')

                    if opcao_vendas == '1':
                        cadastrar_venda()
                    elif opcao_vendas == '2':
                        clear_screen()
                        listar_vendas()
                        t.sleep(5)
                    elif opcao_vendas == '3':
                        consultar_venda()
                        t.sleep(5)
                    elif opcao_vendas == '4':
                        excluir_venda()
                    elif opcao_vendas == '5':
                        break
                    else:
                        print('Opção inválida!')

            elif opcao == '4':
                clear_screen()
                print('Encerrando o programa...')
                t.sleep(2)
                break

            else:
                print('Opção inválida!')

    if name == 'main':
        main()

    create
    database
    loja

    use
    loja
    CREATE
    TABLE
    cliente_loja(
        id_cliente
    INT
    PRIMARY
    KEY
    IDENTITY,
    nome
    VARCHAR(100)
    NOT
    NULL,
    sobrenome
    VARCHAR(100)
    NOT
    NULL,
    cep
    VARCHAR(10)
    NOT
    NULL
    )


    CREATE
    TABLE
    motocicleta_loja(
        id_motocicleta
    INT
    PRIMARY
    KEY
    IDENTITY,
    marca
    VARCHAR(100)
    NOT
    NULL,
    modelo
    VARCHAR(100)
    NOT
    NULL,
    ano
    INT
    NOT
    NULL
    )


    CREATE
    TABLE
    venda(
        id_venda
    INT
    PRIMARY
    KEY
    IDENTITY,
    id_cliente
    INT
    NOT
    NULL,
    id_motocicleta
    INT
    NOT
    NULL,
    valor
    FLOAT
    NOT
    NULL,
    data_venda
    DATETIME
    DEFAULT
    GETDATE(),
    FOREIGN
    KEY(id_cliente)
    REFERENCES
    cliente_loja(id_cliente),
    FOREIGN
    KEY(id_motocicleta)
    REFERENCES
    motocicleta_loja(id_motocicleta)
    )