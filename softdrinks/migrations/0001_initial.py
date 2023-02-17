# Generated by Django 4.1.7 on 2023-02-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='soda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]