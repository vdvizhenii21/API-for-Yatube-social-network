from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Group(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=200,
        help_text="Дайте подробное описание группе"
    )
    description = models.TextField(
        "Текст",
        help_text="Опишите суть группы",
        blank=True
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        "Текст",
        help_text="Дайте короткое описание поста"
    )
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts")
    group = models.ForeignKey(
        Group,
        verbose_name="Выберите группу",
        help_text="Выберите группу из существующих",
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower")
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following")

    class Meta:
        unique_together = ['user', 'following']
