# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'some secret key'

books = ['the first book', 'the second book', 'the third book']

@app.route("/")
def index():
    render_string = '<ul>'

    for book in books:
        render_string += '<li>' + book + '</li>'

    render_string += '</ul>'

    return render_string

@app.route("/book", methods=['POST', 'GET'])
def book():
    _form = request.form

    if request.method == 'POST':
        title = _form["title"]
        books.append(title)
        return redirect(url_for('index'))

    return '''
        <form name="book" action="/book" method="post">
            <input id="title" name="title" type="text" placeholder="add book">
            <button type="submit">Submit</button>
        </form>
        '''

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5200, debug=True)