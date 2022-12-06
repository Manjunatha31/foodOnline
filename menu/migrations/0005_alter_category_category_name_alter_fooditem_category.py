# Generated by Django 4.1.3 on 2022-12-03 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_merge_20221203_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fooditems', to='menu.category'),
        ),
    ]