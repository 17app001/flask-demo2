from flask import Flask, jsonify, render_template
from datetime import datetime
from pm25 import get_pm25_data

app = Flask(__name__)
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
}


@app.route("/pm25")
def get_pm25():

    columns, values = get_pm25_data()
    result = True
    return render_template("./pm25.html", columns=columns, values=values, result=result)


@app.route("/sum/x=<x>&y=<y>")
def sum(x, y):
    total = int(x) + int(y)
    return f"{x}+{y}={total}"


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/books")
def all_books():
    return render_template("./books.html", books=books)


@app.route("/books/<int:id>")
def show_books(id=None):
    if id is not None:
        if id in books:
            return books[id]
        else:
            return jsonify({"error": "Book not found"}), 404
    return jsonify(books)


@app.route("/")
def index():
    date = datetime.now()
    return render_template("./index.html", date=date)


app.run(debug=True)
