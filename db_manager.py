import sqlite3

# Указываем имя файла базы данных
DB_FILE = 'database.db'

def get_connection():
    # Создает подключение к базе данных и возвращает объект соединения.

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Позволяет получать данные в виде словарей
    return conn

def init_db():
    # Инициализация базы данных (создание таблиц).

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            chat_id INTEGER
        )
        ''')
        conn.commit()

def get_users():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    
def get_user_chat_id(chat_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
        return cursor.fetchone()  # Возвращаем только одну запись


def add_user(username, first_name, last_name, chat_id):
    #Добавляет нового пользователя в базу.

    username = username or "unknown"
    first_name = first_name or "unknown"
    last_name = last_name or "unknown"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (username, first_name, last_name, chat_id)
        VALUES (?, ?, ?, ?)
        ''', (username, first_name, last_name, chat_id))
        conn.commit()
