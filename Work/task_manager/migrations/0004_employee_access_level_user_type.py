# Generated by Django 4.2.13 on 2024-06-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_task_is_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='access_level',
            field=models.CharField(choices=[('standard', 'Стандартный'), ('extended', 'Расширенный')], default='standard', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('customer', 'Заказчик'), ('employee', 'Сотрудник')], default='customer', max_length=10),
        ),
    ]
