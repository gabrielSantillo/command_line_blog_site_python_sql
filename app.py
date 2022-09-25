import dbcreds
import mariadb


def get_all_posts():
    conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('CALL get_all_posts()')
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for post in result:
        print("\n",post[0], post[1],)

def post_user_content(user_id):
    content = input("Type your content:\n")
    title = input("Type your title:\n")
    conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('CALL add_post_user(?,?,?)', [user_id, content, title])
    cursor.close()
    conn.close()

def log_in_user():
    username = input("Username: ")
    password = input("password: ")
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

def get_user_selection():
    print("1. Insert a post?")
    print("2. Read all posts?")
    print("3. Quit?")
    user_selection = input("Chose between 1, 2 or 3.")
    return user_selection


def run_app():
    while(True):
        user_id = log_in_user()
        user_selection = get_user_selection()
        if(user_selection == "1"):
            post_user_content(user_id)
        elif(user_selection == "2"):
            get_all_posts()
        elif(user_selection == "3"):
            print("Bye.")
            return
        else:
            print("You must type only numbers between 1, 2 or 3.")
            get_user_selection()


run_app()