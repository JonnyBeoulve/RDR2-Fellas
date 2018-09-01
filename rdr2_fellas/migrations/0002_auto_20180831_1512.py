# Generated by Django 2.1 on 2018-08-31 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdr2_fellas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gamerstyle',
            field=models.CharField(choices=[('Casual', 'Competititor'), ('Moderate', 'Moderate'), ('Hardcore', 'Hardcore')], default='casual', max_length=13),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='platform',
            field=models.CharField(choices=[('PlayStation 4', 'PlayStation 4'), ('Xbox One', 'Xbox One')], default='ps4', max_length=13),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='playstyle',
            field=models.CharField(choices=[('Adventurer', 'Adventurer'), ('Competitor', 'Competititor'), ('Hunter', 'Hunter'), ('Level Grinder', 'Level Grinder'), ('Money Maker', 'Money Maker'), ('Royale Fiend', 'Royale Fiend')], default='adventurer', max_length=13),
        ),
    ]