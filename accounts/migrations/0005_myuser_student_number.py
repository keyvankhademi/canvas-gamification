# Generated by Django 3.0.3 on 2020-04-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_myuser_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='student_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]