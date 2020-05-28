from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    contact = models.ForeignKey(to=Contact,
                                on_delete=models.CASCADE,
                                related_name="addresses")
    address_type = models.CharField(max_length=255)
    line_1 = models.CharField(max_length=255, null=True, blank=True)
    line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)

    def __str__(self):
        output = self.line_1
        if self.line_2:
            output += ", " + self.line_2
        output += f", {self.city}, {self.state}, {self.zip_code}"
        return output
