# Generated by Django 4.2.7 on 2023-11-18 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.CharField(default="Всем привет!", max_length=300),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="profiles.city",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="interests",
            field=models.ManyToManyField(blank=True, null=True, to="profiles.interest"),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]