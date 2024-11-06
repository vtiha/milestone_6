import csv
from faker import Faker
import random

fake = Faker()
num_books = 100
categories = ["Thriller", "Fantasy", "Mystery", "Adventure", "Nonfiction", "Comics", "Poetry", "History", "Art", "Science"]

with open('milestone_9/books.csv', mode='w') as file:

    fieldnames = ['Title', 'Author', 'Category']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(num_books):
        writer.writerow({
            'Title': fake.sentence(nb_words=3),  
            'Author': fake.name(),  
            'Category': random.choice(categories) 
        })

with open('milestone_9/books.csv', mode='r') as file:
    print(file.read())