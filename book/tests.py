from django.test import TestCase
from .models import Book
from django.urls import reverse

class BookTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.book = Book.objects.create(
			title='A good title',
			subtitle='excellent subtitle',
			author='AlisherSharipov',
			isbn='123456',
			)


	def test_book_content(self):
		self.assertEqual(self.book.title, 'A good title')
		self.assertEqual(self.book.subtitle, 'excellent subtitle')
		self.assertEqual(self.book.author, 'AlisherSharipov')
		self.assertEqual(self.book.isbn, '123456')

	def test_book_listview(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'excellent subtitle')
		self.assertTemplateUsed(response, 'book/book_list.html' )