# Generated by Django 3.1.4 on 2020-12-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201203_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', help_text='Min. size 500x750', upload_to='blog_pics'),
        ),
    ]
