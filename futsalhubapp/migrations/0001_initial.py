# Generated by Django 3.0.2 on 2020-02-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('pid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=110)),
                ('lname', models.CharField(max_length=90)),
                ('username', models.CharField(max_length=101)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=70)),
                ('repassword', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]