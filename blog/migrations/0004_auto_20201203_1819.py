# Generated by Django 3.1.4 on 2020-12-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='blog_pics/'),
        ),
    ]
