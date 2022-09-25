import dbcreds
import mariadb

def get_user_id(username, password):
    conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('CALL select_user_id(?,?)', [username, password])
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if(len(result) == 1):
        for id in result:
            return print(id)
    else:
        return print(None)

username = input("Username: ")
password = input("password: ")

get_user_id(username, password)