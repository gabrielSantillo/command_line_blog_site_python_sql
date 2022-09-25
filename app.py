import dbcreds
import mariadb


def get_all_posts():
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    cursor.execute('CALL get_all_posts()')
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for post in result:
        print("\n",post[0], post[1],"\n")

def post_user_content(user_id):
    content = input("Type your content:\n")
    title = input("Type your title:\n")
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    cursor.execute('CALL add_post_user(?,?,?)', [user_id, content, title])
    cursor.close()
    conn.close()

def log_in_user():
    username = input("Username: ")
    password = input("Password: ")
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    cursor.execute('CALL select_user_id(?,?)', [username, password])
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if(len(result) == 1):
        for id in result:
            return id[0]
    else:
        print("Your username or password is incorrect. Try again.")
        return


def get_user_selection():
    print("\n1. Insert a post?")
    print("2. Read all posts?")
    print("3. Quit?")
    user_selection = input("Chose between 1, 2 or 3.\n")
    return user_selection


def run_app():
    user_id = log_in_user()
    if(user_id == None):
        run_app()
    while(True):
        user_selection = get_user_selection()
        if(user_selection == "1"):
            post_user_content(user_id)
        elif(user_selection == "2"):
            get_all_posts()
        elif(user_selection == "3"):
            return
        else:
            print("You must type only numbers between 1, 2 or 3.")


run_app()