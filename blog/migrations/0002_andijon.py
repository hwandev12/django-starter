# Generated by Django 4.1.7 on 2023-04-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Andijon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ovqat', models.CharField(max_length=130)),
                ('text', models.TextField(max_length=700)),
            ],
        ),
    ]
