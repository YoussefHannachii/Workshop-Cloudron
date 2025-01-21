import unittest
from unittest.mock import patch, MagicMock
from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from app import app  # Ensure this matches your actual Flask app import

class TestFlaskApp(unittest.TestCase):

    @patch('app.articles_collection')  # Correct the patch reference here
    def test_index(self, mock_articles_collection):
        mock_articles_collection.find.return_value = [{'title': 'Test Article', 'content': 'Test content', 'author': 'Test author'}]
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Article', response.data)

    @patch('app.articles_collection')  # Correct the patch reference here
    def test_new_article_post(self, mock_articles_collection):
        client = app.test_client()
        response = client.post('/new', data={'title': 'Test', 'content': 'Test content', 'author': 'Test author'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')

    @patch('app.articles_collection')  # Correct the patch reference here
    def test_view_article(self, mock_articles_collection):
        mock_articles_collection.find_one.return_value = {'_id': ObjectId(), 'title': 'Test', 'content': 'Test content', 'author': 'Test author'}
        client = app.test_client()
        response = client.get('/article/605c5b2e8c4a7c14f83096df')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test', response.data)

    @patch('app.articles_collection')  # Correct the patch reference here
    def test_edit_article_post(self, mock_articles_collection):
        mock_articles_collection.find_one.return_value = {'_id': ObjectId(), 'title': 'Test', 'content': 'Test content', 'author': 'Test author'}
        client = app.test_client()
        response = client.post('/edit/605c5b2e8c4a7c14f83096df', data={'title': 'Test updated', 'content': 'Test content updated', 'author': 'Test author updated'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')

    @patch('app.articles_collection')  # Correct the patch reference here
    def test_delete_article(self, mock_articles_collection):
        client = app.test_client()
        response = client.post('/delete/605c5b2e8c4a7c14f83096df')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/')

if __name__ == '__main__':
    unittest.main()
