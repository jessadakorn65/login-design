# Generated by Django 5.0.3 on 2024-12-14 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_pig_breed_pig_owner_pig_status_pig_weight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insemination',
            fields=[
                ('inseminations_id', models.AutoField(primary_key=True, serialize=False)),
                ('insemination_date', models.DateField()),
                ('semen_id', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='inseminations/')),
                ('insemination_result', models.CharField(choices=[('สำเร็จ', 'สำเร็จ'), ('ล้มเหลว', 'ล้มเหลว')], default='ล้มเหลว', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pig_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inseminations', to='myapp.pig')),
            ],
        ),
    ]
