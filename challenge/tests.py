from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Article


# Create your tests here.


class SerializersTests(APITestCase):
    def test_validation_email(self):
        user = {
            'email': 'teste@teste.com',
            'username': 'teste1',
            'password': 'senha123'
        }
        self.client.post('/api/sign-up/', user)

        user2 = {
            'email': 'teste@teste.com',
            'username': 'teste2',
            'password': 'teste123'

        }

        response = self.client.post('/api/sign-up/', user2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validation_username(self):
        user = {
            'email': 'teste@teste.com',
            'username': 'teste1',
            'password': 'senha123'
        }
        self.client.post('/api/sign-up/', user)

        user2 = {
            'email': 'teste2@teste.com',
            'username': 'teste1',
            'password': 'teste123'
        }
        response = self.client.post('/api/sign-up/', user2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validation_article(self):
        author = {
            'id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
            'name': 'José de Alencar',
        }
        AuthorResponse = self.client.post('/api/admin/authors/', author)

        if AuthorResponse.status_code == status.HTTP_201_CREATED:
            article = {
                'author_id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
                'title': 'Lucíola',
                'category': 'Romance',
                'summary': 'kfnsdofnsodnf',
                'first_paragraph': 'ksdmfsofsofmsfmsomfsofmosdf',
                'body': 'fsdfsdfsfd'
            }
            ArticleResponse = self.client.post('/api/admin/articles/', article)
            self.assertEqual(ArticleResponse.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validation_trueArticle(self):
        author = {
            'id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
            'name': 'José de Alencar',
        }
        AuthorResponse = self.client.post('/api/admin/authors/', author)

        if AuthorResponse.status_code == status.HTTP_201_CREATED:
            article = {
                'author_id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
                'title': 'Lucíola',
                'category': 'Romance',
                'summary': 'kfnsdofnsodnf',
                'first_paragraph': 'ksdmfsofsofmsfmsomfsofmosdf',
                'body': 'fsdfsdfgdfgdfgdfgdfgdgdfgdgdgdgddfgdfgdfdfgdgdgdgdfgdfgdfgdfgdfgdgfsfd'
            }
            ArticleResponse = self.client.post('/api/admin/articles/', article)
            self.assertEqual(ArticleResponse.status_code, status.HTTP_201_CREATED)

    def test_str_function(self):
        author = Author.objects.create(name='Zíbia Gasparetto')
        self.assertEqual(str(author), 'Zíbia Gasparetto')

    def test_authorized(self):
        article = {
            'author_id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
            'title': 'Lucíola',
            'category': 'Romance',
            'summary': 'kfnsdofnsodnf',
            'body': 'fsdfsdfgdfgdfgdfgdfgdgdfgdgdgdgddfgdfgdfdfgdgdgdgdfgdfgdfgdfgdfgdgfsfd'
        }
        ArticleResponse = self.client.post('/api/admin/articles/', article)
        self.assertEqual(ArticleResponse.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_first_paragraph_on_body(self):
        author = {
            'id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
            'name': 'José de Alencar',
        }
        AuthorResponse = self.client.post('/api/admin/authors/', author)

        if AuthorResponse.status_code == status.HTTP_201_CREATED:
            article = {
                'author_id': '9d8dcf07-4d0e-4377-b27a-499ee172d338',
                'title': 'Lucíola',
                'category': 'Romance',
                'summary': 'kfnsdofnsodnf',
                'first_paragraph': 'fsdfsdfgdfgdfgdfgdfgdgdfgdgdgdgddfgdfgdfdfgdgdgdgdfgdfgdfgdfgdfgdgfsfd',
                'body': 'fsdfsdfgdfgdfgdfgdfgdgdfgdgdgdgddfgdfgdfdfgdgdgdgdfgdfgdfgdfgdfgdgfsfd,'
                        'sdoasndasdasdknassdasjndajdasldmaonfajssdasfa.'
            }
            ArticleResponse = self.client.post('/api/admin/articles/', article)
            self.assertEqual(ArticleResponse.status_code, status.HTTP_201_CREATED)

