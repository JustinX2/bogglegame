from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        with self.client as client:
            response = client.get('/')
            self.assertIn('board', session)
            self.assertIn(b'<div id="game-board">', response.data)

    def test_valid_word(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S']
                ]
            response = client.get('/check-word?word=test')
            self.assertEqual(response.json['result'], 'ok')
