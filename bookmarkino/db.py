import sqlite3
from bookmarkino.bookmark import Bookmark

class DB:
    connection = None
    def connect(self, db_file=None):
        self.connection = sqlite3.connect("bookmarkino.db" if db_file == None else db_file)

    def sync_tables(self):
        cur = self.connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS bookmarks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    url TEXT NOT NULL
                    )""")

    def fetch_bookmarks(self):
        cur = self.connection.cursor()
        res = cur.execute("SELECT * FROM bookmarks")
        bookmarks = []
        for row in res.fetchall():
            bookmarks.append(Bookmark(row[0], row[1]))
        return bookmarks

    def insert_bookmark(self, url):
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO bookmarks (url) VALUES ('{url}')")
        self.connection.commit()

    def close(self):
        if self.connection is None:
            return
        self.connection.close()
