from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='somoseco_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='somoseco_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    complexity = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    reward = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    proposed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposesd_issues')

    def __str__(self):
        return f'{self.title} - {self.proposed_by.username}'

class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='campaigns')
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_campaigns')
    members = models.ManyToManyField(User, related_name='campaigns')

    def __str__(self):
        return f'{self.post.title} - {self.leader.username}'
