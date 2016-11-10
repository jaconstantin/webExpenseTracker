# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('entrydate', models.DateField(db_column='entryDate')),
                ('entrytime', models.TimeField(db_column='entryTime')),
                ('prcurrency', models.CharField(max_length=4, db_column='prCurrency')),
                ('prvalue', models.DecimalField(decimal_places=4, db_column='prValue', max_digits=19)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
