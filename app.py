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
    print("3. Read only your posts?")
    print("4. See all usernames?")
    print("5. Wanna see posts based in a username?")
    print("6. Quit?")
    user_selection = input("Chose between 1, 2, 3, 4, 5 or 6.\n")
    return user_selection

def get_user_post(user_id):
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    cursor.execute('CALL get_post_by_id(?)', [user_id])
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for post in result:
        print("\n",post[0], post[1],"\n")

def get_all_usernames():
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    cursor.execute('CALL get_all_usernames()')
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for post in result:
        print("\n",post[0],"\n")

def get_post_by_username():
    username = input("What is the username you want see the posts?\n")
    try:
        conn = mariadb.connect(password=dbcreds.pasword, user=dbcreds.user, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Something went wrong. The appropriate person has been notified.")
    cursor = conn.cursor()
    cursor.execute('CALL get_post_by_username(?)', [username])
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for post in result:
        print("\n",post[0], post[1],"\n")


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
            get_user_post(user_id)
        elif(user_selection == "4"):
            get_all_usernames()
        elif(user_selection == "5"):
            get_post_by_username()
        elif(user_selection == "6"):
            return
        else:
            print("You must type only numbers between 1, 2, 3, 4, 5 or 6.")


run_app()