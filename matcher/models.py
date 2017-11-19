from __future__ import unicode_literals

from django.db import models


class SurveyResponse(models.Model):
    """ survey questions """
    q1 = models.CharField(max_length=16, help_text="")
    q2 = models.CharField(max_length=16, help_text="")
    q3 = models.CharField(max_length=16, help_text="")
    q4 = models.CharField(max_length=16, help_text="")
    q5 = models.CharField(max_length=16, help_text="")


class ServiceSchool(models.Model):
    """ table for serivce school listings """
    name = models.CharField(max_length=64, help="name of service school")


class ServiceSchoolResponse(models.Model):
    """ table for service school questions """
    school = models.ForeignKey(ServiceSchool)
    survey = models.ForeignKey(SurveyResponse)


class Raiser(models.Model):
    """ table for potential raisers """
    name = models.CharField(max_length=64, help="name of raiser")


class RaiserSurveyResponse(models.Model):
    """ table to track raiser survey responses """
    raiser = models.ForeignKey(Raiser)
    survey = models.ForeignKey(SurveyResponse)
