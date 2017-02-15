from django.db import models

class Data(models.Model):
    data_text = models.CharField(max_length=200)
    data_money = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
