# Generated by Django 4.1.7 on 2023-04-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_namangan_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=20)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
        ),
        migrations.AlterModelOptions(
            name='namangan',
            options={'verbose_name': "Namangan Qo'shish", 'verbose_name_plural': 'Namangan'},
        ),
    ]
