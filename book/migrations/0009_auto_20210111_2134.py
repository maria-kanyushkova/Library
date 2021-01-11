# Generated by Django 3.1.3 on 2021-01-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_publishers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='author',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='author',
            name='surname',
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='book.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, to='book.Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='labels',
            field=models.ManyToManyField(blank=True, to='book.Label'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishers',
            field=models.ManyToManyField(blank=True, to='book.Publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ManyToManyField(blank=True, to='book.Series'),
        ),
    ]
