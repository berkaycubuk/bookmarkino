# Bookmarkino v1.0.0
# Programmed by Berkay Çubuk <berkay@berkaycubuk.com> 2024
#
# Simple program to save your bookmarks separate from the browser.
import sys, getopt
from bookmarkino.db import DB

def version():
    print("v1.0.0")

def usage():
    print("Bookmarkino v1.0.0")
    print("Simple program to save your bookmarks separate from the browser.\n")
    print("-h --help: Learn how to use Bookmarkino")
    print("-v --version: Prints version")
    print("-l --list: Lists saved bookmarks")
    print("-i --insert: Inserts bookmark and requires an address after it.")
    print("\tbookmarkino -i https://berkaycubuk.com")

def main():
    argv = sys.argv[1:]

    db = DB()
    db.connect()

    db.sync_tables()

    try:
        opts, args = getopt.getopt(argv, "hvi:l", ["help", "version", "insert", "list"])
    except getopt.GetoptError as err:
        print(err)
        return

    for o, a in opts:
        if o in ("-v", "--version"):
            version()
        elif o in ("-h", "--help"):
            usage()
        elif o in ("-i", "--insert"):
            db.insert_bookmark(a)
            print("Bookmark {} inserted".format(a))
        elif o in ("-l", "--list"):
            bookmarks = db.fetch_bookmarks()
            for bookmark in bookmarks:
                print("{}: {}".format(bookmark.id,bookmark.url))

    if len(opts) == 0:
        usage()


    db.close()

if __name__ == "__main__":
    main()
