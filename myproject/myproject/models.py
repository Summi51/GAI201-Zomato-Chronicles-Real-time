from django.db import models

class Feedback(models.Model):
    order_id = models.CharField(max_length=10)
    rating = models.PositiveIntegerField()
    review = models.TextField()

    def __str__(self):
        return f"Feedback for Order {self.order_id}"
