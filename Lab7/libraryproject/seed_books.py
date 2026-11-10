import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "libraryproject.settings"
)

import django
django.setup()

from apps.bookmodule.models import Book

books = [
    ("Continuous Delivery", "J.Humble and D. Farley", 120.00, 3),
    ("Reversing: Secrets of Reverse Engineer", "E. Eilam", 97.00, 2),
    ("The Hundred-Page Machine Learning Book", "Andriy Burkov", 100.00, 4),
    ("Python and Django", "Test Author", 150.00, 3),
]

for title, author, price, edition in books:
    Book.objects.update_or_create(
        title=title,
        defaults={
            "author": author,
            "price": price,
            "edition": edition,
        },
    )

print("Sample data inserted successfully.")

for book in Book.objects.order_by("id"):
    print(
        f"{book.id} | {book.title} | "
        f"{book.author} | {book.price} | {book.edition}"
    )
