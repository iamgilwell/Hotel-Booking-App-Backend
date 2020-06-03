# Generated by Django 3.0.6 on 2020-06-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('number_of_guests', models.TextField(blank=True, null=True)),
                ('room_number', models.TextField(blank=True, null=True)),
                ('active', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Inactive', max_length=20)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
