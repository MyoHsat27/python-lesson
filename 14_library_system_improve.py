def load_books():
    try:
        file = open('books.txt', 'r')
        books = file.read().split('\n')
        books.pop()
        file.close()
        return books
    except FileNotFoundError:
        return []


def save_books(books):
    file = open('books.txt', 'w')
    for book in books:
        file.write(book + "\n")
    file.close()


def list():
    if len(books) == 0:
        print("There is no book")
    else:
        print("List of books :")
        for book in books:
            print(f"[{books.index(book) + 1}] {book}")


def register():
    new_book = input("Enter the new book name : ")
    books.append(new_book)
    save_books(books)
    print(f"[{new_book}] is added to the book list")


def search():
    keyword = input("Search : ")
    for i in range(len(books)):
        if keyword.lower() in books[i].lower():
            print(f"[{i + 1}] : {books[i]}")


def delete():
    book_index = int(input("Enter the book number that you want to delete : "))
    deleted_book = books.pop(book_index - 1)
    save_books(books)
    print(f"[{deleted_book}] is removed")


# Load books from file
books = load_books()

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
