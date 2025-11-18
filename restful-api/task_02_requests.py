#!/usr/bin/python3


import requests
import csv


"""
Module that fetches posts from the JSONPlaceholder API and either prints them
or saves them into a CSV file.
"""


def fetch_and_print_posts():
    """
    Fetch posts from the API and print the status code and each post title.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code:", r.status_code)

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from the API and save their id, title, and body into posts.csv.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
        data = []

        for post in posts:
            new_dic = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            data.append(new_dic)

        with open('posts.csv', 'w', newline="", encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
