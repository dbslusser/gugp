from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField


example = (("", ""), ("", ""), ("", ""), ("", ""), )
time_commitment_choices = (("1-6 months", "1-6 months"), ("6-12 months", "6-12 months"),
                           ("12-18 months", "12-18 months"), ("part-time", "part-time"), )
meeting_requirement_choices = (("weekly", "weekly"), ("bi-weekly", "bi-weekly"),
                               ("monthly", "monthly"), ("other", "other"), )
gear_choices = (("Flat collar", "Flat collar"), ("Head collar", "Head collar"),
                ("Prong collar", "Prong collar"), ("Martingale collar", "Martingale collar"),
                ("coke/training collar", "coke/training collar"), ("No pull harness", "No pull harness"),
                ("other", "other"),
                )
record_requirement_choices = (("weekly", "weekly"), ("bi-weekly", "bi-weekly"),
                                ("monthly", "monthly"), ("other", "other"), )
training_update_choices = (("quarterly", "quarterly"), ("monthly", "monthly"),
                           ("None", "None"), ("other", "other"), )
training_style_choices = (("positive reinforcement", "positive reinforcement"),
                  ("negative reinforcement", "negative reinforcement"),
                  ("positive punishment", "positive punishment"),
                  ("negative punishment", "negative punishment"), )
placement_choices = (("yes", "yes"), ("no", "no"), ("depending on recipient", "depending on recipient"),
                     ("other", "other"), )
food_reward_choices = (("marker word", "marker word"), ("clicker", "clicker"))
obedience_choices = (("specific task training", "specific task training"), ("basic obedience", "basic obedience"))


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

    def __str__(self):
        return self.name


class SchoolContact(GenericContact):
    """ contact fields specific to schools """
    school = models.ForeignKey(School)
    role = models.CharField(max_length=16, help_text="role or title")


class Expense(models.Model):
    """ table for raising expense """
    school = models.ForeignKey(School)
    name = models.CharField(max_length=16, help_text="name of expense")
    percent = models.IntegerField(help_text="percent that the school covers")

    def __str__(self):
        return self.name


class Policy(models.Model):
    """ table for school policies """
    school = models.ForeignKey(School)
    name = models.CharField(max_length=16, help_text="name of policy")
    description = models.TextField(max_length=255, help_text="name of policy", blank=True, null=True)
    link = models.URLField(help_text="link to policy URL/document", blank=True, null=True)

    def __str__(self):
        return self.name


class SchoolSurvey(models.Model):
    """ raiser requirements from school """
    school = models.OneToOneField(School)
    q01 = models.CharField(max_length=16, choices=time_commitment_choices, help_text="What is the time commitment do you need from your puppy raisers?")
    # q02 = models.CharField(max_length=16, help_text="")
    q03 = models.CharField(max_length=16, help_text="What states can a puppy raiser reside when raising for your organization?")
    q04 = models.CharField(max_length=16, choices=meeting_requirement_choices, help_text="Are raisers required to attend regular meetings or training sessions? If so how often")
    q05 = MultiSelectField(max_length=32, choices=gear_choices, help_text="What type of gear can a raise use?")
    q06 = models.CharField(max_length=32, choices=training_style_choices, help_text="What type of training style does your organization use?")
    q07 = models.CharField(max_length=16, choices=food_reward_choices, help_text="If you use food rewards to do you use a marker word or clicker?")
    q08 = models.BooleanField(help_text="Do raisers do public access socialization and training?")
    q09 = models.CharField(max_length=32, choices=obedience_choices, help_text="Do your raisers do specific task training or just basic obedience?")
    q10 = models.IntegerField(help_text="At what age do puppies return to your organization for formal training?")
    q11 = models.CharField(max_length=16, help_text="Does the organization provide advisors or guidance to their raisers?")
    # q12 = models.CharField(max_length=16, help_text="")
    q13 = models.CharField(max_length=16, choices=training_update_choices, help_text="Do you offer updates to raisers when their puppy returns for formal training?")
    q14 = models.BooleanField(help_text="Do you have a formal graduation ceremony for your graduates?")
    q15 = models.CharField(max_length=32, choices=placement_choices, help_text="Do you allow raisers to know who their puppy is placed with?")
    q16 = models.FloatField(help_text="What percent of your dogs graduate from your program?")
    q17 = models.BooleanField(help_text="If a dog doesn't graduate from your program do you work with other programs for placement?")
    q18 = models.BooleanField(help_text="Do your puppy raisers have an opportunity to adopt their puppy if it doesn't graduate from your program?")
    q19 = models.BooleanField(help_text="If a dog is placed anywhere other than a graduate of your program or their puppy raiser, will the raiser be told where their puppy is placed and what type of work it will be doing?")
    q20 = models.BooleanField(help_text="Are puppies evaluated for suitability while they are in the raiser's home or only when they return for formal training?")
    # q21 = models.CharField(max_length=16, help_text="")
    q22 = models.IntegerField(help_text="At what age do you spay and neuter your dogs?")
    q23 = models.CharField(max_length=16, choices=training_update_choices, help_text="What are the record keeping requirements of your puppy raisers?")


class Service(models.Model):
    """ type to service animal provides (i.e.) vision aid """
    name = models.CharField(max_length=16, help_text="name of service this school trains for")
    description = models.TextField(max_length=255, null=True, blank=True)


class SchoolServiceCatalog(models.Model):
    """ listing of services the school provides """
    school = models.ForeignKey(School)
    service = models.ForeignKey(Service)


class Raiser(GenericContact):
    """ table for raisers """
    experience = models.IntegerField(blank=True, null=True, help_text="")


class RaiserSurvey(models.Model):
    """ survey responses from potential raisers """
    raiser = models.OneToOneField(Raiser)
    q1 = models.CharField(max_length=16, help_text="")
    q2 = models.CharField(max_length=16, help_text="")
    q3 = models.CharField(max_length=16, help_text="")
    q4 = models.CharField(max_length=16, help_text="")
    q5 = models.CharField(max_length=16, help_text="")
