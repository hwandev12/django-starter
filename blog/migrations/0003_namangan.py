# Generated by Django 4.1.7 on 2023-04-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_andijon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Namangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat', models.CharField(max_length=60)),
                ('viloyat_haqida', models.TextField(max_length=700)),
                ('odam_soni', models.IntegerField()),
                ('ortacha_yosh', models.IntegerField()),
                ('tumanlar_soni', models.IntegerField()),
            ],
        ),
    ]