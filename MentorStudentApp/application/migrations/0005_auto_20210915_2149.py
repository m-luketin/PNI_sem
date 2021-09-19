from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "my_initial_data.json")


class Migration(migrations.Migration):
    dependencies = [
        ('application', '0004_auto_20210915_2008'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]