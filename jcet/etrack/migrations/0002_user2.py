# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('entrydate', models.DateField(db_column='entryDate')),
                ('entrytime', models.TimeField(db_column='entryTime')),
                ('prcurrency', models.CharField(max_length=4, db_column='prCurrency')),
                ('prvalue', models.DecimalField(decimal_places=4, max_digits=19, db_column='prValue')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
