# Generated by Django 5.1.1 on 2024-10-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]