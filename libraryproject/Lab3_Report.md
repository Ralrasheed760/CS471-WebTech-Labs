# Lab 3 Report – Django and MVT Architecture

**Course:** CS471 – Web Technologies  
**Lab:** 3  
**Topic:** Django URLs, Views, and HTML Templates

---

## Objective

The objective of this lab was to understand how Django processes HTTP requests using URL patterns, view functions, and HTML templates.

I continued working on the Django project created in Lab 2, which includes two applications: `bookmodule` and `usermodule`.

Throughout this lab, I implemented seven tasks and tested their functionality using the Django development server and a web browser.

---

## Task 1: Build the First View Function and URL Mapping

I started by creating my first view function named `index` inside `apps/bookmodule/views.py`.

I imported `HttpResponse` from Django and used it to return a simple text message.

I then updated the main URL configuration in `libraryproject/urls.py` to connect the `/books/` URL to the `index` view.

**Implementation:**

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```

**Testing:**

| Test URL | Output |
|---|---|
| `http://127.0.0.1:8000/books/` | `Hello, world!` |

**Result:** I successfully displayed `Hello, world!` in the browser, confirming that the URL was correctly connected to the view function.

---

## Task 2: Add Parameters with HTTP Requests

I modified the `index` view to retrieve a name from an HTTP GET request using `request.GET.get("name")`.

If the URL did not contain a name parameter, the view used `world!` as the default value.

**Implementation:**

```python
def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)
```

**Testing:**

| Test URL | Output |
|---|---|
| `http://127.0.0.1:8000/books/` | `Hello, world!` |
| `http://127.0.0.1:8000/books/?name=Razan` | `Hello, Razan` |

**Result:** I successfully tested both URLs and confirmed that the view retrieved the name parameter and displayed the corresponding greeting.

---

## Task 3: Build a Second View with URL Parameters

I created a second view function named `index2` in `apps/bookmodule/views.py`.

The function accepts an integer parameter called `val1` and displays its value using `HttpResponse`.

I added a URL pattern using `<int:val1>` to allow Django to extract the integer directly from the URL.

**Implementation:**

```python
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))
```

**Testing:**

I tested the function using three different integer values.

| Test | URL | Output |
|---|---|---|
| 1 | `/books/index2/3/` | `value1 = 3` |
| 2 | `/books/index2/10/` | `value1 = 10` |
| 3 | `/books/index2/0/` | `value1 = 0` |

**Result:** All three tests were successful. I confirmed that the view correctly received and displayed each integer value passed through the URL.

---

## Task 4: Create a Simple HTML Template

I created a templates directory inside the `apps` folder with the following structure:

```text
apps/
└── templates/
    └── bookmodule/
        └── index.html
```

Inside `index.html`, I added a simple HTML heading.

**HTML Implementation:**

```html
<h1>Hello from a template!</h1>
```

I updated `libraryproject/settings.py` to specify the location of the templates directory.

**Settings Configuration:**

```python
import os

TEMPLATE_DIR = os.path.join(BASE_DIR, "apps" + os.sep + "templates")
```

I also updated the `TEMPLATES` configuration:

```python
'DIRS': [TEMPLATE_DIR],
```

Next, I imported Django's `render` function and modified the `index` view to return the HTML template instead of a direct `HttpResponse`.

**View Implementation:**

```python
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")
```

**Testing:**

| Test URL | Output |
|---|---|
| `http://127.0.0.1:8000/books/` | `Hello from a template!` |

**Result:** I successfully displayed the HTML heading in the browser, confirming that Django located and rendered the template correctly.

---

## Task 5: Render Variables in an HTML Template

I modified `index.html` to display a dynamic name using Django's template variable syntax.

**HTML Implementation:**

```html
<h1>Hello from {{ name }}!</h1>
```

I then updated the `index` view to pass the name variable to the template using a context dictionary.

**View Implementation:**

```python
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})
```

**Testing:**

| Test URL | Output |
|---|---|
| `http://127.0.0.1:8000/books/?name=Razan` | `Hello from Razan!` |

**Result:** I successfully displayed `Hello from Razan!` in the browser, confirming that the context variable was passed correctly from the view to the HTML template.

---

## Task 6: Define URL Patterns for Each Application

I organized the URL configuration by creating a separate `urls.py` file for each Django application.

The files I created were:

- `apps/bookmodule/urls.py`
- `apps/usermodule/urls.py`

I moved the book-related URL patterns into the `bookmodule` URL configuration.

**Bookmodule URL Configuration:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2)
]
```

I created the `usermodule/urls.py` file with an empty `urlpatterns` list, as required in the lab.

**Usermodule URL Configuration:**

```python
from django.urls import path

urlpatterns = [
]
```

I then modified the main `libraryproject/urls.py` file to use Django's `include()` function.

**Main URL Configuration:**

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls"))
]
```

**Testing:**

After reorganizing the URL patterns, I tested both views again.

| Test | URL | Output |
|---|---|---|
| 1 | `/books/?name=Razan` | `Hello from Razan!` |
| 2 | `/books/index2/3/` | `value1 = 3` |

**Result:** Both tests were successful. I confirmed that the application-level URL configurations worked correctly after using `include()`.

---

## Task 7: Create a URL, View, and HTML Template to Display Book Details

In the final task, I created a new view function named `viewbook` in `apps/bookmodule/views.py`.

The function accepts a book ID and retrieves the corresponding book information from two predefined dictionaries.

**View Implementation:**

```python
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}

    targetBook = None

    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2

    context = {'book':targetBook}

    return render(request, 'bookmodule/show.html', context)
```

I then added a new URL pattern to `apps/bookmodule/urls.py`:

```python
path('<int:bookId>', views.viewbook)
```

Next, I created a new HTML template named `show.html` inside `apps/templates/bookmodule/`.

**HTML Implementation:**

```html
<h4>ID: {{ book.id }}</h4>
<h4>Title: {{ book.title }}</h4>
<h4>Authors</h4>
<p>{{ book.author }}</p>
<h4>Description</h4>
<p>Description here</p>
```

**Testing:**

I tested the book details page using the two book IDs specified in the lab.

**Test 1: Book ID 123**

URL: `http://127.0.0.1:8000/books/123`

Output:

- ID: 123
- Title: Continuous Delivery
- Authors: J. Humble and D. Farley
- Description: Description here

**Test 2: Book ID 456**

URL: `http://127.0.0.1:8000/books/456`

Output:

- ID: 456
- Title: Secrets of Reverse Engineering
- Authors: E. Eilam
- Description: Description here

**Result:** I successfully displayed the correct book information for both IDs, confirming that the view retrieved the appropriate book details based on the URL parameter.

---

## Conclusion

In Lab 3, I successfully completed all seven tasks by implementing Django URL routing, view functions, HTTP GET parameters, dynamic URL parameters, HTML templates, context variables, and application-level URL configurations.

I started by displaying a simple `Hello, world!` message, then added name parameters and tested three different integer values.

Next, I created HTML templates, passed dynamic variables from views to templates, and organized URL patterns into separate application files.

Finally, I implemented a book details page and successfully tested it using two different book IDs.

Through this lab, I gained practical experience with Django's Model-View-Template (MVT) architecture and learned how URLs, views, and templates work together to process HTTP requests and generate dynamic web pages.
