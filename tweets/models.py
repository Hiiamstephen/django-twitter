from django.db import models
from django.contrib.auth.models import User
from utils.time_helpers import utc_now

class Tweet(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        help_text='who posts the tweet',

    )
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    # # create time each time of update
    # update_at = models.DateTimeField(auto_now=True)

    @property
    def hours_to_now(self):
         return (utc_now() - self.created_at).seconds // 3600

    def __str__(self):
        # 这里是你执行 print(tweet instance) 的时候会显示的内容
        return f'{self.created_at} {self.user}: {self.content}'
