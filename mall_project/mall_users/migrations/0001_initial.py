# Generated by Django 5.1 on 2024-08-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MallUserClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('user_pw', models.CharField(max_length=64, verbose_name='User Password')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Registered Date Time')),
            ],
            options={
                'verbose_name': 'Mall Users',
                'verbose_name_plural': 'Mall Users',
                'db_table': 'mall_users_db',
            },
        ),
    ]
