"""
Pull FROM API
https://www.googleapis.com/books/v1/volumes?q=michael%20crighton&key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8

"""
import requests


def get_books(author):
    url = f'https://www.googleapis.com/books/v1/volumes?q={author}&key=AIzaSyB6Z5mdvSohshY0VhSmArRoKkDOjZNG7b8'
    r = requests.get(url)
    books = r.json()
    books_list = {'books': books['items']}
    return books_list
