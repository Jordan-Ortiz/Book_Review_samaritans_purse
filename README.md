# Book_Review_samaritans_purse
Book Review Django App


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="./django_samaritans_purse/Library/books/static/books/book_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Django Book Review App</h3>




<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#requirements">Requirements</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
  </ol>
</details>




<!-- ABOUT THE PROJECT -->
## About The Project

Welcome to the Book Review, Each Book is pulled from Google's Book API by author and Book's ID. 

Non-Users:  
* They are able to use the search form by author
* They are able register as a user
* They are able to see all reviews from other users. 
* They are NOT able to write a review or favorite a book. 

Users:  
* Login and Logout
* They are able to search for books by author
* They are able to write reviews of each book
* They are able to save favorite books by clicking the star and favorite books will be stored in database 
* They will be able to find their favorite books on My Favorite Book Page
* They will be able to see their own reviews and update or delete them


### Built With


* [Django 3.2](https://docs.djangoproject.com/en/3.2/)
* [Python](https://www.python.org/)
* [Bootstrap](https://getbootstrap.com)



## Requirements

* python==3.9.0
* django==3.2
* django-crispy-forms==1.11.2
* requests==2.25.1

## Getting Started


Steps
1. Check if django is installed and django is on version 3.2 
```sh
   $ python -m django --version
   ```
If Django is not installed or you need latested version please follow this link: ["How to install Django"](https://docs.djangoproject.com/en/3.2/topics/install/)

2. Clone the repository or Pull Repository 
```sh
   $ git clone https://github.com/Jordan-Ortiz/Book_Review_samaritans_purse
   ``` 
3. Install a virtual environment 
 ```sh
   $ pip install virtualenv 
   ``` 
   
4. Set up virtual environment by changing Directories into Book_Review_samaritans_purse/django_samaritans_purse and run virtualenv venv
 ```sh
   $ cd Book_Review_samaritans_purse/django_samaritans_purse && virtualenv venv
   ``` 

5. Make sure to install requirements from above
 ```sh
   pip install requests
   ```
 ```sh
   pip install django-crispy-forms
   ```
6. In Terminal change directories to Book_Review_samaritans_purse/django_samaritans_purse/Library/ and runserver on 0:8000 
 ```sh
   cd Book_Review_samaritans_purse/django_samaritans_purse/Library/ && python manage.py runserver 0:8000
   ```
7. Have Fun With The Book Review Application!

8. When Done ^C (control + C) in Terminal to end session



