from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['CI-CD']
articles_collection = db['articles']

@app.route('/')
def index():
    articles = articles_collection.find()
    return render_template('index.html', articles=articles)

@app.route('/new', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        articles_collection.insert_one({'title': title, 'content': content, 'author': author})
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/article/<article_id>')
def view_article(article_id):
    article = articles_collection.find_one({'_id': ObjectId(article_id)})
    return render_template('article.html', article=article)

@app.route('/edit/<article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    article = articles_collection.find_one({'_id': ObjectId(article_id)})
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        articles_collection.update_one(
            {'_id': ObjectId(article_id)},
            {'$set': {'title': title, 'content': content, 'author': author}}
        )
        return redirect(url_for('index'))
    return render_template('edit.html', article=article)

@app.route('/delete/<article_id>', methods=['POST', 'GET'])
def delete_article(article_id):
    articles_collection.delete_one({'_id': ObjectId(article_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
