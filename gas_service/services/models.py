

from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    TYPE_CHOICES = [
        ('gas_leak', 'Gas Leak'),
        ('billing_query', 'Billing Query'),
        ('service_installation', 'Service Installation'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    submission_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_request_type_display()} by {self.user.username} - {self.get_status_display()}"
