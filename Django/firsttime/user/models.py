from django.db import models

class Course(models.Model):
    card_image = models.CharField(max_length=200, null=True)
    card_title = models.CharField(max_length=200, null=True)
    card_text = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    videos = models.CharField(max_length=200, null=True)


    # Add other fields as necessary

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    user_name = models.CharField(max_length=200, null=True)
    user_feedback = models.TextField(blank=True, null=True)