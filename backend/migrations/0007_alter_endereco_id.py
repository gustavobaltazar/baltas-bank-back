# Generated by Django 4.1 on 2022-10-04 19:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_endereco_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
