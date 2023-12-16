from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields if you need
    # For example, if you want to use email as the primary login field:
    email = models.EmailField(unique=True)

    # If you are using email as the primary login identifier, uncomment the next two lines:
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.username  # Or return self.email if using email as primary

class Conversation(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name='conversations')

# Message Model
from .encryption import encrypt_message, decrypt_message

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    encrypted_content = models.BinaryField()  # Store encrypted text
    timestamp = models.DateTimeField(auto_now_add=True)

    def set_content(self, value):
        # Encrypt message content before saving
        self.encrypted_content = encrypt_message(value)

    def get_content(self):
        # Decrypt message content for access
        return decrypt_message(self.encrypted_content)

    content = property(get_content, set_content)

    class Meta:
        ordering = ['timestamp']