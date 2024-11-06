import csv

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"'{self.title}' by {self.author} (Category: {self.category})"


class Shelf:
    def __init__(self, categories):
        self.categories = categories
        self.books = []

    def add_book(self, book):
        if book.category in self.categories:
            self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda book: (book.category, book.author))

    def __str__(self):
        return f"Shelf with categories: {', '.join(self.categories)}, Books: {len(self.books)}"


def read_books_from_csv(file_name):
    books = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = Book(row['Title'], row['Author'], row['Category'])
            books.append(book)
    return books


def organize_books_on_shelves(books, categories, num_shelves, max_books_per_shelf):

    shelf_categories = [categories[i::num_shelves] for i in range(num_shelves)]  
    
    shelves = [Shelf(categories) for categories in shelf_categories]

    for book in books:
        for shelf in shelves:
            if book.category in shelf.categories:
                if len(shelf.books) < max_books_per_shelf:
                    shelf.add_book(book)
                    break

    for shelf in shelves:
        shelf.sort_books()
    
    return shelves


def print_books_on_shelves(shelves):
    for shelf in shelves:
        print(f"\n{shelf}")
        for book in shelf.books:
            print(f"  {book}")


if __name__ == '__main__':
    categories = ["Thriller", "Fantasy", "Mystery", "Adventure", "Nonfiction", "Comics", "Poetry", "History", "Art", "Science"]
    num_shelves = 4
    max_books_per_shelf = 35  # штучне обмеження, щоб на одній полиці не було 70 книг, а на інших по 10
    books = read_books_from_csv('milestone_8/books.csv')
    shelves = organize_books_on_shelves(books, categories, num_shelves, max_books_per_shelf)
    print_books_on_shelves(shelves)
