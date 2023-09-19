# Library MGMT Program
def list():
    for book in books:
        print(f"[{books.index(book) + 1}] : {book}")

def register():
    new_book = input("Enter the new book name : ")
    books.append(new_book)
    print(f"[{new_book}] is added to the book list")

def search():
    keyword = input("Search : ") # new
    for book in books: # "book1", "book2" , "book3", "New Book"
        if keyword.lower() in book.lower():
            print(f"[{books.index(book) + 1}] : {book}")

def delete():
    book_index = int(input("Enter the book number that you want to delete : "))
    deleted_book = books[book_index - 1]
    sure = input(f"Are you sure? You want to delete [{deleted_book}] (Y/N) : ").lower()
    if sure == "y":
        books.pop(book_index - 1)
        print(f"[{deleted_book}] is removed")


books = ["book1", "book2", "book3"]
commands = ("list", "register", "search", "delete", "quit")
command_string = """
Library
------------
# list
# register
# search
# delete
# quit
------------"""
print(command_string)
while True:
    cmd_input = input("Enter the command : ").lower()

    if cmd_input == "list":
        list()
    elif cmd_input == "register":
        register()
    elif cmd_input == "search":
        search()
    elif cmd_input == "delete":
        delete()
    elif cmd_input == "quit":
        print("Thank you for using our Library MGMT")
        break
    else:
        print(command_string)
        print("Invalid Command")