# Generated by Django 4.2.7 on 2023-12-10 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_records_email_alter_records_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название процедуры')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена процедуры')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Процедура',
                'verbose_name_plural': 'Процедуры',
            },
        ),
    ]
