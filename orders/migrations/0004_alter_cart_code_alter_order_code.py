# Generated by Django 4.2 on 2023-10-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_alter_cart_code_alter_order_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="code",
            field=models.CharField(default="636C9CA94", max_length=9),
        ),
        migrations.AlterField(
            model_name="order",
            name="code",
            field=models.CharField(default="A6CA7279893B763", max_length=15),
        ),
    ]
