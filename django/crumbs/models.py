# imports, Django core
from django.db import models


class Expense(models.Model):
    """Represents the Expense object."""
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True)
    #date = models.DateTimeField('date of expense')
    date = models.DateField('date of expense', blank=True, null=True)
    purpose = models.CharField(max_length=200, blank=True, null=True)
    incurred_by = models.ForeignKey(
        'people.User',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String to represent the User object (in Admin site etc.)
        """
        return self.purpose

    class Meta:
        ordering = ('amount',)


# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
class Receipt(models.Model):
    receipt = models.FileField(upload_to='receipts/')
    #receipt = models.ImageField(upload_to='receipts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)