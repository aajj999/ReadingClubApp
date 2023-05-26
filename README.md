# ReadingClubApp

Small project using Django REST Framework.  
Consists of three models : Book, Author and Type.  
There is one-to-many relation between Author and Book and one many-to-many between Book and Type.  
All models can be found in */ReadingClubApp/ReadingClub/RCAPP/models.py*

### Usage
1. In main folder execute : **python manage.py runserver**  
2. In browser you can display and add new objects.  
    For example by going to ***http://127.0.0.1:8000/db/books/*** where you will be able to add new books to the database.
