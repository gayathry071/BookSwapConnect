# Generated by Django 5.0.3 on 2024-03-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_delete_tbl_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_level', models.CharField(max_length=15)),
                ('quality_rule', models.CharField(max_length=50)),
            ],
        ),
    ]