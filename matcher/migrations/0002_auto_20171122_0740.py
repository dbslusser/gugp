# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of policy', max_length=16)),
                ('description', models.TextField(blank=True, help_text='name of policy', max_length=255, null=True)),
                ('link', models.URLField(blank=True, help_text='link to policy URL/document', null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.School')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolServiceCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.School')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of service this school trains for', max_length=16)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='policies',
            name='school',
        ),
        migrations.RemoveField(
            model_name='schoolsurvey',
            name='q1',
        ),
        migrations.RemoveField(
            model_name='schoolsurvey',
            name='q2',
        ),
        migrations.RemoveField(
            model_name='schoolsurvey',
            name='q3',
        ),
        migrations.RemoveField(
            model_name='schoolsurvey',
            name='q4',
        ),
        migrations.RemoveField(
            model_name='schoolsurvey',
            name='q5',
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q01',
            field=models.CharField(choices=[('1-6 months', '1-6 months'), ('6-12 months', '6-12 months'), ('12-18 months', '12-18 months'), ('part-time', 'part-time')], default=1, help_text='What is the time commitment do you need from your puppy raisers?', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q03',
            field=models.CharField(default=1, help_text='What states can a puppy raiser reside when raising for your organization?', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q04',
            field=models.CharField(choices=[('weekly', 'weekly'), ('bi-weekly', 'bi-weekly'), ('monthly', 'monthly'), ('other', 'other')], default=1, help_text='Are raisers required to attend regular meetings or training sessions? If so how often', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q05',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Flat collar', 'Flat collar'), ('Head collar', 'Head collar'), ('Prong collar', 'Prong collar'), ('Martingale collar', 'Martingale collar'), ('coke/training collar', 'coke/training collar'), ('No pull harness', 'No pull harness'), ('other', 'other')], default=1, help_text='What type of gear can a raise use?', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q06',
            field=models.CharField(choices=[('positive reinforcement', 'positive reinforcement'), ('negative reinforcement', 'negative reinforcement'), ('positive punishment', 'positive punishment'), ('negative punishment', 'negative punishment')], default=1, help_text='What type of training style does your organization use?', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q07',
            field=models.CharField(choices=[('marker word', 'marker word'), ('clicker', 'clicker')], default=1, help_text='If you use food rewards to do you use a marker word or clicker?', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q08',
            field=models.BooleanField(default=1, help_text='Do raisers do public access socialization and training?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q09',
            field=models.CharField(choices=[('specific task training', 'specific task training'), ('basic obedience', 'basic obedience')], default=1, help_text='Do your raisers do specific task training or just basic obedience?', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q10',
            field=models.IntegerField(default=1, help_text='At what age do puppies return to your organization for formal training?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q11',
            field=models.CharField(default=1, help_text='Does the organization provide advisors or guidance to their raisers?', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q13',
            field=models.CharField(choices=[('quarterly', 'quarterly'), ('monthly', 'monthly'), ('None', 'None'), ('other', 'other')], default=1, help_text='Do you offer updates to raisers when their puppy returns for formal training?', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q14',
            field=models.BooleanField(default=1, help_text='Do you have a formal graduation ceremony for your graduates?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q15',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('depending on recipient', 'depending on recipient'), ('other', 'other')], default=1, help_text='Do you allow raisers to know who their puppy is placed with?', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q16',
            field=models.FloatField(default=1, help_text='What percent of your dogs graduate from your program?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q17',
            field=models.BooleanField(default=1, help_text="If a dog doesn't graduate from your program do you work with other programs for placement?"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q18',
            field=models.BooleanField(default=1, help_text="Do your puppy raisers have an opportunity to adopt their puppy if it doesn't graduate from your program?"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q19',
            field=models.BooleanField(default=1, help_text='If a dog is placed anywhere other than a graduate of your program or their puppy raiser, will the raiser be told where their puppy is placed and what type of work it will be doing?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q20',
            field=models.BooleanField(default=1, help_text="Are puppies evaluated for suitability while they are in the raiser's home or only when they return for formal training?"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q22',
            field=models.IntegerField(default=1, help_text='At what age do you spay and neuter your dogs?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolsurvey',
            name='q23',
            field=models.CharField(choices=[('quarterly', 'quarterly'), ('monthly', 'monthly'), ('None', 'None'), ('other', 'other')], default=1, help_text='What are the record keeping requirements of your puppy raisers?', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='raisersurvey',
            name='raiser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='matcher.Raiser'),
        ),
        migrations.DeleteModel(
            name='Policies',
        ),
        migrations.AddField(
            model_name='schoolservicecatalog',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.Service'),
        ),
    ]
