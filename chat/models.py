from django.db import models
from django.conf import settings


class Message(models.Model):
    msg_content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=50)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.msg_content

    def get_messages(self):
        return self.objects.all()