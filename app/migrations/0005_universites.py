# Generated by Django 4.2 on 2025-02-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_arrondissement_app_arrondi_nom_284d81_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Universite',
                'verbose_name_plural': 'Universites',
            },
        ),
    ]
