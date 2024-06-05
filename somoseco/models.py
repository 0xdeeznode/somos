from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField()

    def __str__(self):
        return self.username

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
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
