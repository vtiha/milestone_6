# Book Organization Project

This project is designed to organize books into a catalog, with automated sorting onto shelves by category and with a limit on the number of books per shelf.

## File Descriptions

### 1. `Room_for_book.html`
This file contains the UML diagram, created after coding, which represents the structure of the project's classes. The diagram includes:
- The `Book` class, representing individual books with attributes for title, author, and category.
- The `Shelf` class, representing a shelf, with methods for organizing books, sorting by author within a category, and limiting the number of books on each shelf.

### 2. `book_generator.py`
This file generates the `books.csv` file with 100 random books. Each book includes:
- Title
- Author
- Category, chosen randomly from a predefined list of categories: `["Thriller", "Fantasy", "Mystery", "Adventure", "Nonfiction", "Comics", "Poetry", "History", "Art", "Science"]`

### 3. `books.csv`
This file, created by `book_generator.py`, contains a list of randomly generated books for use in the main project code.

### 4. `main.py`
This file implements the main functionality of the project, including:
- Distributing books onto shelves based on their categories.
- Sorting books alphabetically by authors within each category on a shelf.
- Limiting the number of books per shelf.
