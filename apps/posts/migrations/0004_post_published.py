# Generated by Django 4.0.5 on 2022-06-11 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_category_slug_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="published",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="게시 일"
            ),
        ),
    ]