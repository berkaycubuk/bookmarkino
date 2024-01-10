import unittest, os
from bookmarkino.db import DB

class DBTests(unittest.TestCase):
    def __remove_test_db_if_exists(self):
        if os.path.exists("bookmarkino_test.db"):
            os.remove("bookmarkino_test.db")

    def test_db_connect(self):
        self.__remove_test_db_if_exists()

        db = DB()
        db.connect("bookmarkino_test.db")
        db.close()

        # check is file created
        self.assertEqual(os.path.exists("bookmarkino_test.db"), True)

    def test_db_sync_tables(self):
        self.__remove_test_db_if_exists()

        db = DB()
        db.connect("bookmarkino_test.db")
        db.sync_tables()

        cur = db.connection.cursor()
        cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bookmarks'")
        self.assertEqual(cur.fetchone()[0],1)

        db.close()

if __name__ == '__main__':
    unittest.main()
