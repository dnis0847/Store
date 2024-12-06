# Generated by Django 5.1.3 on 2024-11-15 10:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_product_options_product_publish_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-publish', 'title'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='Store_produ_publish_043a9d_idx',
        ),
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
