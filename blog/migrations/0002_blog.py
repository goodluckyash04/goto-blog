# Generated by Django 4.2 on 2023-04-21 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('pic', models.FileField(default='default.jpg', upload_to='blogimage')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogger')),
            ],
        ),
    ]
