# Generated by Django 3.2 on 2022-03-16 10:25

from django.db import migrations, models
import expense.models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0009_alter_expense_reciept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='reciept',
            field=models.FileField(upload_to=expense.models.upload_name),
        ),
    ]
