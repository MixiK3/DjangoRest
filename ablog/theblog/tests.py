from django.test import TestCase
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm
from .models import Post, Category

'''Тесты для моделей'''
class PostModelTestCase(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.test_post = Post.objects.create(
            title='Test Post Title',
            author=self.test_user,

        )

    def test_title_field_max_length(self):
        max_length = self.test_post._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_header_image_field(self):
        field = self.test_post._meta.get_field('header_image')
        self.assertEquals(field.null, True)
        self.assertEquals(field.blank, True)
        self.assertEquals(field.upload_to, 'images/')

    def test_title_tag_field_max_length(self):
        max_length = self.test_post._meta.get_field('title_tag').max_length
        self.assertEquals(max_length, 255)

    def test_author_field(self):
        field = self.test_post._meta.get_field('author')
        self.assertEquals(field.related_model, User)

    def test_body_field(self):
        field = self.test_post._meta.get_field('body')
        self.assertEquals(field.blank, True)
        self.assertEquals(field.null, True)
        self.assertEquals(field.__class__.__name__, 'RichTextField')


class CategoryModelTestCase(TestCase):

    def setUp(self):
        self.test_post = Category.objects.create(
            name='Name test',
        )

    def test_name_field_max_length(self):
        max_length = self.test_post._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)


'''Тесты форм'''
class PostFormTest(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(
            username='testuser',
            password='12345'
        )

    def test_form_validity(self):
        form = PostForm(data={
            'title': 'Test title',
            'title_tag': 'Test tag',
            'author': self.author.id,
            'category': 'Choice 1',
            'type_of_articles': 'Type 1',
            'body': 'Test body',
            'snippet': 'Test snippet',
            'header_image': 'test_image.jpg'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        form = PostForm(data={
            'title': '',
            'title_tag': '',
            'author': self.author.id,
            'category': '',
            'type_of_articles': 'Type 1',
            'body': 'Test body',
            'snippet': 'Test snippet',
            'header_image': 'test_image.jpg'
        })
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(
            username='testuser',
            password='12345'
        )

    def test_form_comment_validity(self):
        form = CommentForm(data={
            'name': 'Test title',
            'body': 'Test tag',
        })
        self.assertTrue(form.is_valid())

    def test_form_comment_invalidity(self):
        form = CommentForm(data={
            'name': '',
            'body': '',

        })
        self.assertFalse(form.is_valid())