from django.db import models


class History(models.Model):
    text = models.TextField()  # The input text
    result = models.CharField(max_length=20)  # The classification result
    model_type = models.CharField(max_length=20)  # The model used (even, odd, or lora)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the classification

    def __str__(self):
        return f"{self.text} - {self.result} ({self.model_type})"
