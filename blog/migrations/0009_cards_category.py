# Generated by Django 4.1.7 on 2023-04-13 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
