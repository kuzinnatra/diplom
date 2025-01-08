from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from library.models import Book, Author
from users.models import User
from django.contrib.auth.models import Group


class LibraryTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@sky.pro', password='123qwe')
        self.special_group = Group.objects.create(name='Librarian')
        self.user.groups.add(self.special_group)
        print("test_setUp")

        self.client.login(email='test@sky.pro', password='123qwe')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.force_authenticate(user=self.user)

    def test_create_author(self):
        response = self.client.post(
            '/library/author/create/',
            data={'name': 'Автор_1', }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_author(self):
        author = Author.objects.create(name='Автор_1')
        response = self.client.patch(
            f'/library/author/{author.pk}/update',
            data={'name': 'Автор_1_измененный', }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_create_book(self):
        author = Author.objects.create(name='Автор_1')
        data = {
             'name': 'Книга_первая',
             'availability': True,
             'genre': 'Приключение',
             'author': author.pk
        }

        response = self.client.post(
            '/library/books/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_books_update(self):
        author = Author.objects.create(name='Автор_1')
        book = Book.objects.create(name='Книга_первая', availability=True, genre='Приключение', author=author)
        response = self.client.patch(
            f'/library/books/{book.pk}/update',
            data={'name': 'Книга_вторая',}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_author_delete(self):
        author = Author.objects.create(name='Автор_1')
        response = self.client.delete(
            f'/library/author/{author.pk}/delete/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_book_delete(self):
        author = Author.objects.create(name='Автор_1')
        book = Book.objects.create(name='Книга_первая', availability=True, genre='Приключение', author=author)
        response = self.client.delete(
            f'/library/books/{book.pk}/delete/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_books_list(self):
        author = Author.objects.create(name='Автор_1')
        book = Book.objects.create(name='Книга_первая', availability=True, genre='Приключение', author=author)
        response = self.client.get(
            '/library/books/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_authors_list(self):
        author = Author.objects.create(name='Автор_1')
        response = self.client.get(
            '/library/author/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_create(self):
        response = self.client.post(
            '/users/register/',
            data={'name': 'test_user', 'email': 'test_user@sky.pro', 'password': '123qwe'}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_user(self):
        user = User.objects.create(name='test_user', email='test_user@sky.pro', password='123qwe')
        response = self.client.patch(
            f'/users/user/{user.pk}/update',
            data={'name': 'Bad', }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_301_MOVED_PERMANENTLY
        )

    def test_user_delete(self):
        user = User.objects.create(name='test_user', email='test_user@sky.pro', password='123qwe')
        response = self.client.delete(
            f'/users/user/{user.pk}/delete/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
    def test_user_list(self):
        user = User.objects.create(name='test_user', email='test_user@sky.pro', password='123qwe')
        response = self.client.get(
            '/users/user/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


