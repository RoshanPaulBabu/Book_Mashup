# Generated by Django 5.0.4 on 2024-04-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.AddField(
            model_name='book',
            name='historical_period',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='related_books',
            field=models.ManyToManyField(blank=True, to='books.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]