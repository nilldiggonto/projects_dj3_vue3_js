from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    MESSAGE = 'message'
    FOLLOWER = 'follower'
    LIKE = 'like'
    CHOICES = (
        (MESSAGE,'Message'),
        (FOLLOWER,'Follower'),
        (LIKE,'like')
    )

    to_user             = models.ForeignKey(User,related_name='notifications',on_delete=models.CASCADE)
    notification_type   = models.CharField(max_length=20,choices=CHOICES)
    is_read             = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    created_by          = models.ForeignKey(User,related_name='createnotifications',on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.created_by)
