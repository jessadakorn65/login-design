# Generated by Django 5.0.3 on 2024-12-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pig_id', models.CharField(max_length=100)),
                ('pig_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('breed', models.CharField(max_length=100)),
            ],
        ),
    ]