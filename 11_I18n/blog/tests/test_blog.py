from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Post, Tag


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='4efefwefe'
        )

        self.post = Post.objects.create(
            title='A good title',
            article='Nice body content',
            author=self.user
        )
        self.tag = Tag.objects.create(
            title='A good tag',
            slug='Agoodtag'
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), f'/blog/post/{self.post.slug}/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.article}', 'Nice body content')

    def test_post_list_view(self):
        url = reverse('blog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_post_detail_view(self):
        url = reverse('post_detail_url', kwargs={'slug': self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view_GET(self):
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('add_post_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')

    def test_post_create_view_POST(self):
        new_post = {
            'title': 'New title',
            'article': 'New text',
            'author': self.user
        }
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('add_post_url')
        response = self.client.post(url, new_post, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        self.assertEqual(len(Post.objects.all()), 2)
        slug = Post.objects.get(title='New title').slug
        self.assertRedirects(response, reverse('post_detail_url', kwargs={'slug': slug}))

    def test_post_update_view_GET(self):
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('update_post_url', kwargs={'slug': self.post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/update_post.html')

    def test_post_update_view(self):
        update_post = {
            'title': 'Updated title',
            'article': 'Updated text'
        }
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('update_post_url', kwargs={'slug': self.post.slug})
        response = self.client.post(url, update_post)
        self.assertEqual(response.status_code, 302)
        slug = Post.objects.get(title='Updated title').slug
        self.assertRedirects(response, reverse('post_detail_url', kwargs={'slug': slug}))

    def test_tags_list_view(self):
        url = reverse('tags_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good tag')
        self.assertTemplateUsed(response, 'blog/tags_list.html')

    def test_tag_detail_view(self):
        url = reverse('tag_detail_url', kwargs={'slug': self.tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good tag')
        self.assertTemplateUsed(response, 'blog/tag_detail.html')
        self.assertEqual(Tag.objects.count(), 1)

    def test_tag_create_view_GET(self):
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        url = reverse('add_tag_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_tag.html')

    def test_tag_create_view_POST(self):
        tag_count = Tag.objects.count()
        new_tag = {
            'title': 'New tag',
            'slug': 'Newslug',
        }
        login = self.client.login(username='testuser',
                                  password='4efefwefe')
        self.assertTrue(login)
        url = reverse('add_tag_url')
        response = self.client.post(url, new_tag, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New tag')
        self.assertEqual(Tag.objects.count(), tag_count + 1)
        self.assertRedirects(response, reverse('tags_list'))

