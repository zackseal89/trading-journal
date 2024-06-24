import sqlite3

def create_connection():
    connection = sqlite3.connect('trades.db')
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY,
        date TEXT,
        time TEXT,
        symbol TEXT,
        position TEXT,
        entry_price REAL,
        exit_price REAL,
        profit_loss REAL,
        trade_size INTEGER,
        strategy TEXT,
        indicators TEXT,
        reason TEXT,
        stop_loss REAL,
        take_profit REAL,
        emotions TEXT,
        emotional_triggers TEXT,
        distractions TEXT,
        mistakes TEXT,
        comments TEXT,
        market_conditions TEXT,
        news_events TEXT
    )''')
    connection.commit()

if __name__ == '__main__':
    conn = create_connection()
    create_table(conn)
    conn.close()

