from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com",password="secret"
        )

        cls.post = Post.objects.create(
            title="Test Title",
            body="Test Body",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.body, "Test Body")
        self.assertEqual(self.post.author.username, self.user.username)
        self.assertEqual(str(self.post), "Test Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_url_exists_at_location_detailview(self):
        resp = self.client.get("/post/1/")
        self.assertEqual(resp.status_code, 200)

    def test_post_listview(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Test Body")
        self.assertTemplateUsed(resp, "home.html")

    def test_post_detailview(self):
        resp = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(resp, "Test Title")
        self.assertContains(resp, "Test Body")
        self.assertTemplateUsed(resp, "post_detail.html")