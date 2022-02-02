import sqlite3


# Add the data where saved all information about tasks
def add_data():
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS data(
    ID          INTEGER         NOT NULL,
    Text        STRING (1, 256) NOT NULL,
    VALUE       INTEGER (1, 10) NOT NULL,
    ENUMERATING INTEGER (1, 10) NOT NULL
                                
    )
""")

    connect.commit()

# Using for know what "enumerating_text" equal
def list_date(user_id: int):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()

    cursor.execute("SELECT COUNT(*) FROM data WHERE ID = ? LIMIT 1", (user_id,))
    (res,) = cursor.fetchone()
    result = res
    return result


# Adding tasks to data
def add_to_date(user_id: int, user_message: str, message_value: int, enumerate_text: int):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()

    cursor.execute("INSERT INTO data VALUES (?,?,?,?)", (user_id, user_message, message_value, enumerate_text))
    connect.commit()


# This function for return all results for user. It`s would sending in answer message "ЗАДАЧИ"
def show_date(user_id: int):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT ENUMERATING, Text, VALUE FROM data WHERE ID = ? ORDER BY VALUE DESC LIMIT 10", (user_id,))
    connect.commit()
    return cursor.fetchall()


def show_date_enumerating(user_id: int):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT ENUMERATING FROM data WHERE ID = ? ORDER BY ENUMERATING LIMIT 10", (user_id,))
    connect.commit()
    return cursor.fetchall()


# Delete tasks from data. deleted_text would equal answer of user
def delete_date(deleted_text: int, user_id: int):
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM data WHERE ENUMERATING = ? AND ID = ?", (deleted_text, user_id))
    connect.commit()


add_data()

