# Generated by Django 2.2.6 on 2019-10-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
    ]
