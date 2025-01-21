from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://mongo:27017/")  # Use the service name 'mongo'
db = client['CI-CD_Project']
articles_collection = db['article']

# Initialize Flask-RESTX API
api = Api(app, version='1.0', title='Article Management API',
          description='A simple API for managing articles using Flask and MongoDB')

# Define the article model for Swagger documentation
article_model = api.model('Article', {
    'id': fields.String(readonly=True, description='The unique identifier of the article'),
    'title': fields.String(required=True, description='The title of the article'),
    'content': fields.String(required=True, description='The content of the article'),
    'author': fields.String(required=True, description='The author of the article'),
})

# Index route to render all articles (non-API)
@app.route('/')
def index():
    articles = articles_collection.find()
    return render_template('index.html', articles=articles)

# Route to create a new article (non-API)
@app.route('/new', methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        articles_collection.insert_one({'title': title, 'content': content, 'author': author})
        return redirect(url_for('index'))
    return render_template('new.html')

# API Route: Get all articles
@api.route('/api/articles')
class ArticleList(Resource):
    def get(self):
        """Get all articles"""
        articles = articles_collection.find()
        return [{'id': str(article['_id']), 'title': article['title'], 'content': article['content'], 'author': article['author']} for article in articles]

    @api.expect(article_model)
    def post(self):
        """Create a new article"""
        data = api.payload
        new_article = {
            'title': data['title'],
            'content': data['content'],
            'author': data['author']
        }
        article = articles_collection.insert_one(new_article)
        return {'id': str(article.inserted_id), **new_article}, 201

# API Route: Get a single article
@api.route('/api/article/<article_id>')
class Article(Resource):
    def get(self, article_id):
        """Get a single article by its ID"""
        article = articles_collection.find_one({'_id': ObjectId(article_id)})
        if article:
            return {'id': str(article['_id']), 'title': article['title'], 'content': article['content'], 'author': article['author']}
        return {'message': 'Article not found'}, 404

    @api.expect(article_model)
    def put(self, article_id):
        """Update an article"""
        data = api.payload
        updated_article = {
            'title': data['title'],
            'content': data['content'],
            'author': data['author']
        }
        articles_collection.update_one(
            {'_id': ObjectId(article_id)},
            {'$set': updated_article}
        )
        return {'id': article_id, **updated_article}

    def delete(self, article_id):
        """Delete an article"""
        articles_collection.delete_one({'_id': ObjectId(article_id)})
        return {'message': 'Article deleted'}, 204

# API Route to delete an article (non-API)
@app.route('/delete/<article_id>', methods=['POST', 'GET'])
def delete_article(article_id):
    articles_collection.delete_one({'_id': ObjectId(article_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
