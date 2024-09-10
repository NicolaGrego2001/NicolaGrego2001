import mysql.connector

# dettagli connessione
details = {
    'host': "172.17.0.2",
    'user': "prod",
    'password': "password",
    'database': "gestionale"
}


def init_db_connection(db_details: dict) -> mysql.connector.MySQLConnection:
    # inizializzo connessione
    return mysql.connector.connect(**db_details)


def read():
    mydb = init_db_connection(details)  # ottengo connessione

    # creo cursor
    mycursor = mydb.cursor(dictionary=True)

    # query
    query = 'SELECT * FROM test'

    # eseguo query
    mycursor.execute(query)

    # ottengo risultati
    results = mycursor.fetchall()

    # chiudo connessione
    mydb.close()

    return results

def read_condition():
    mydb = init_db_connection(details)  # ottengo connessione

    # creo cursor
    mycursor = mydb.cursor(dictionary=True)

    # query
    query = 'SELECT * FROM test WHERE nome = %s'
    value = ('Pippo',)

    # eseguo query
    mycursor.execute(query, value)

    # ottengo risultati
    results = mycursor.fetchall()

    # chiudo connessione
    mydb.close()

    return results

def write():
    mydb = init_db_connection(details)  # ottengo connessione

    # creo cursor
    mycursor = mydb.cursor()

    # query
    query = 'INSERT INTO test (nome, cognome) VALUES (%s, %s)'
    values = ('Pippo', 'De Pluti')

    # eseguo query
    mycursor.execute(query, values)

    # commit
    mydb.commit()

    # chiudo connessione
    mydb.close()

def write_multiple():
    mydb = init_db_connection(details)  # ottengo connessione

    # creo cursor
    mycursor = mydb.cursor()

    # query
    query = 'INSERT INTO test (nome, cognome) VALUES (%s, %s)'
    values = [('Pippo', 'De Pluti'), ('Mario', 'Rossi'), ('Pippo', 'Verdi')]

    # eseguo query
    mycursor.executemany(query, values)

    # commit
    mydb.commit()

    # chiudo connessione
    mydb.close()

def edit():
    mydb = init_db_connection(details)  # ottengo connessione

    # creo cursor
    mycursor = mydb.cursor()

    # query
    query = 'UPDATE test SET cognome = %s WHERE nome = %s'
    values = ('Bianchi', 'Pippo')

    # eseguo query
    mycursor.execute(query, values)

    # commit
    mydb.commit()

    # chiudo connessione
    mydb.close()

def truncate():
    """
    Attenzione!!!
    :return:
    """
    mydb = init_db_connection(details)  # ottengo connessione

    # creo cursor
    mycursor = mydb.cursor()

    # query
    query = 'TRUNCATE TABLE test'

    # eseguo query
    mycursor.execute(query)

    # commit
    mydb.commit()

    # chiudo connessione
    mydb.close()

def main():
    truncate()
    print(f"Primo step")
    print(f"Lettura iniziale")
    print(read())

    print(f"Scrivo nuovo record")
    write()
    print(read())

    print(f"Modifico record")
    edit()
    print(read())

    print(f"Pulisco")
    truncate()

    print(f"Secondo step")
    print(f"Lettura iniziale")
    print(read())

    print(f"Scrivo tanti records")
    write_multiple()

    print(f"Leggo con condizione")
    print(read_condition())

    print(f"Pulisco")
    truncate()



if __name__ == "__main__":
    main()