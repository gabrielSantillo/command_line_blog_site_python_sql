import dbcreds
import mariadb

def post_user_content(user_id):
    content = input("Type your content:\n")
    title = input("Type your title:\n")
    conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('CALL add_post_user(?,?,?)', [user_id, content, title])
    cursor.close()
    conn.close()

def get_user_id(username, password):
    conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('CALL select_user_id(?,?)', [username, password])
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if(len(result) == 1):
        for id in result:
            return id[0]
    else:
        return None

username = input("Username: ")
password = input("password: ")
user_id = get_user_id(username, password)
post_user_content(user_id)