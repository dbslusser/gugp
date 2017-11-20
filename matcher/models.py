from __future__ import unicode_literals

from django.db import models


class GenericContact(models.Model):
    """ Abstract table for generic contacts """
    first_name = models.CharField(max_length=16, help_text="first name")
    last_name = models.CharField(max_length=16, help_text="last name")
    phone = models.CharField(max_length=16, help_text="phone number")
    email = models.EmailField(max_length=64, help_text="email address")
    address_1 = models.CharField(max_length=32, help_text="address line 1")
    address_2 = models.CharField(max_length=32, blank=True, null=True, help_text="address line 2")
    city = models.CharField(max_length=32, help_text="city")
    state = models.CharField(max_length=16, help_text="state")
    country = models.CharField(max_length=16, help_text="country")

    class Meta:
        abstract = True


class School(models.Model):
    """ table for service schools """
    name = models.CharField(max_length=64, help_text="name of service school")
    url = models.URLField(max_length=64, help_text="website")
    address_1 = models.CharField(max_length=32, help_text="address line 1")
    address_2 = models.CharField(max_length=32, blank=True, null=True, help_text="address line 2")
    city = models.CharField(max_length=32, help_text="city")
    state = models.CharField(max_length=16, help_text="state")
    country = models.CharField(max_length=16, help_text="country")


class SchoolContact(GenericContact):
    """ contact fields specific to schools """
    school = models.ForeignKey(School)
    role = models.CharField(max_length=16, help_text="role or title")


class Expense(models.Model):
    """ table for raising expense """
    school = models.ForeignKey(School)
    name = models.CharField(max_length=16, help_text="name of expense")
    percent = models.IntegerField(help_text="percent that the school covers")


class Policies(models.Model):
    """ table for school policies """
    school = models.ForeignKey(School)
    name = models.CharField(max_length=16, help_text="name of policy")
    link = models.URLField(help_text="link to policy URL/document", blank=True, null=True)


class SchoolSurvey(models.Model):
    """ raiser requirements from school """
    school = models.OneToOneField(School)
    q1 = models.CharField(max_length=16, help_text="")
    q2 = models.CharField(max_length=16, help_text="")
    q3 = models.CharField(max_length=16, help_text="")
    q4 = models.CharField(max_length=16, help_text="")
    q5 = models.CharField(max_length=16, help_text="")


class Raiser(GenericContact):
    """ table for raisers """
    experience = models.IntegerField(blank=True, null=True, help_text="")


class RaiserSurvey(models.Model):
    """ survey responses from potential raisers """
    raiser = models.ForeignKey(Raiser)
    q1 = models.CharField(max_length=16, help_text="")
    q2 = models.CharField(max_length=16, help_text="")
    q3 = models.CharField(max_length=16, help_text="")
    q4 = models.CharField(max_length=16, help_text="")
    q5 = models.CharField(max_length=16, help_text="")
