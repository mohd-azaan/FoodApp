# Generated by Django 5.0.2 on 2024-05-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('item_description', models.TextField(blank=True)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
