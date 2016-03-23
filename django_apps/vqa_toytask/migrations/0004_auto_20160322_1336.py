# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vqa_toytask', '0003_auto_20160322_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to=b'input_image.jpg'),
        ),
    ]
