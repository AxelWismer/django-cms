# Generated by Django 4.2.5 on 2023-12-27 21:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_alter_client_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AlterField(
            model_name='client',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]