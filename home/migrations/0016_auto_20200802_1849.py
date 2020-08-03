# Generated by Django 3.0.8 on 2020-08-02 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200802_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Location'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='home.Tags'),
        ),
    ]
