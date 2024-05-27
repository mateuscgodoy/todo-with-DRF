from django.db import models


class TodoModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        ordering = ["created_at"]
