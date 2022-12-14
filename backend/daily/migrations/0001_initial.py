# Generated by Django 3.2.14 on 2022-07-27 13:47

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('univ', markdownx.models.MarkdownxField()),
                ('study', markdownx.models.MarkdownxField()),
                ('other', markdownx.models.MarkdownxField()),
                ('first_meet', markdownx.models.MarkdownxField()),
                ('wanna_do', markdownx.models.MarkdownxField()),
                ('summary', markdownx.models.MarkdownxField()),
                ('isOpen', models.BooleanField(default=True)),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='daily.evaluation')),
            ],
        ),
    ]
