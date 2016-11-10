######################################################################################
#tried out the inspectdb feature of django to auto gen the class from an existing table
#   * Make sure each model has one field with primary_key=True -> makemigrations will auto generate one...
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# also note sure if the indes were properly defined...
#####################################################################################


from django.db import models

# Create your models here.

class User1(models.Model):
    entrydate = models.DateField(db_column='entryDate')  # Field name made lowercase.
    entrytime = models.TimeField(db_column='entryTime')  # Field name made lowercase.
    prcurrency = models.CharField(db_column='prCurrency', max_length=4)  # Field name made lowercase.
    prvalue = models.DecimalField(db_column='prValue', max_digits=19, decimal_places=4)  # Field name made lowercase.
    description = models.CharField(max_length=100)

###created this next table due to problems on trying to use an existing sql table
###this was done from sratch

class User2(models.Model):
    entrydate = models.DateField(db_column='entryDate')  # Field name made lowercase.
    entrytime = models.TimeField(db_column='entryTime')  # Field name made lowercase.
    prcurrency = models.CharField(db_column='prCurrency', max_length=4)  # Field name made lowercase.
    prvalue = models.DecimalField(db_column='prValue', max_digits=19, decimal_places=4)  # Field name made lowercase.
    description = models.CharField(max_length=100)