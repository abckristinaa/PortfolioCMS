# Generated by Django 2.1.5 on 2019-04-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0006_auto_20190412_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Logos',
            },
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='logo',
        ),
    ]
