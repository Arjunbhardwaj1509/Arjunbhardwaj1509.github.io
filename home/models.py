from django.db import models

# Contact model definition
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=12, null=False)
    desc = models.TextField(null=True, blank=True)
    namecompany = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name  # Return the correct 'Name' field
