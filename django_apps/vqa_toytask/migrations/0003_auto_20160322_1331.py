# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vqa_toytask', '0002_auto_20160322_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(default=b'input_image.jpg', upload_to=b''),
        ),
    ]
