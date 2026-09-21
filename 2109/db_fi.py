import oracledb
USUARIO = "rm571211"
SENHA = "231207"
HOST = "oracle.fiap.com.br"
PORTA = 1521
SERVICE_NAME = "ORCL"


dsn = oracledb.makedsn (
    HOST,
    PORTA,
    service_name = SERVICE_NAME
)

try:
    conn = oracledb.connect(
        user = USUARIO,
        password = SENHA,
        dsn = dsn
    )

    print("===========================")
    print("CONEXAP REALIZADA COM SUCESSO")
    print("===========================")
except oracledb.Error as erro:
    print("erro ao conectar no banco")
    print(erro)

    exit()



cursor = conn.cursor()
print("Cursor criado com sucesso")


print("=================")
print("CADASTRO DE PET")
print("=================")

tipo_pet = input("digie o tipo do pet: ")
nome_pet = input("digie o nome do pet: ")
idade = int(input("digie a idade do pet: "))

sql = """
    insert into petshop
    (
    id_pet
    tipo_pet.
    nome_pet,
    idade
    )
    values
    (
    :id_pet
    :tipo_pet,
    :nome_pet,
    :idade
    )
    """

cursor.execute(
    sql,
    tipo_pet = tipo_pet,
    nome_pet = nome_pet,
    idade = idade
)

conn.commit()
print("pet cadastrado")
print("programa finalizado")



def incluir_pet():
    print(" cadastro")

    id_pet = int(input("digite o id"))
    tipo_pet = input("digita o tipo")
    nome_pet = input("digita o nome")
    idade = int(input("digita a idade"))
    sql = """
    insert into petshop
    (
        id_pet,
        tipo_pet,
        nome_pet,
        idade
    )
    values
    (
        :id_pet,
        :tipo_pet,
        :nome_pet,
        :idade
    )
    """

try:
    cursor.execute(
        sql,
        id_pet = id_pet,
        tipo_pet = tipo_pet,
        nome_pet = nome_pet,
        idade = idade
    )
except oracledb.Error as erro:
    print("erro ao cadastrar")
    print(erro)

    exit()


def consular_pets():

    print("=== consulta")
    cursor.execute(
        sql = """
                select
                    id_pet,
                    tipo_pet,
                    nome_pet,
                    idade
                from petshop
                order by id_pet
                """
    )

    cursor.execute(sql)
    pets = cursor.fetchall()
    if len(pets) ==0:
        print("nenhuma")

    else:
        for pet in pets:
            print(f"id: {pet[0]}")
            print(f"tipo: {pet[1]}")
            print(f"nome: {pet[2]}")
            print(f"idade: {pet[3]}")

    