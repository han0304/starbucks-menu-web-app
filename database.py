import sqlite3
from pathlib import Path

# 將資料庫檔案放在目前專案資料夾
DB_PATH = Path(__file__).with_name("starbucks.db")


def get_connection():
    """建立 SQLite 資料庫連線"""
    return sqlite3.connect(DB_PATH)


def init_db():
    """建立飲品資料表"""
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drinks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title_cn TEXT NOT NULL,
                title_en TEXT NOT NULL,
                UNIQUE(title_cn, title_en)
            )
        """)

        conn.commit()

    finally:
        conn.close()



def insert_drinks(drinks):
    """將飲品資料寫入資料庫，避免重複新增"""

    # 統一整理名稱中的多餘空白
    cleaned_drinks = [
        (" ".join(title_cn.split()), " ".join(title_en.split()))
        for title_cn, title_en in drinks
    ]

    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO drinks (title_cn, title_en)
            VALUES (?, ?)
        """, cleaned_drinks)

        conn.commit()

    finally:
        conn.close()



def get_all_drinks():
    """讀取資料庫中的所有飲品"""
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, title_cn, title_en
            FROM drinks
            ORDER BY id
        """)

        rows = cursor.fetchall()

        return [
            {
                "id": row[0],
                "title_cn": row[1],
                "title_en": row[2]
            }
            for row in rows
        ]

    finally:
        conn.close()
