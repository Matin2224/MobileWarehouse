# Generated by Django 4.2 on 2024-11-29 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('nationality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=255)),
                ('screen_size', models.PositiveIntegerField()),
                ('availability_status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=20)),
                ('assembling_country', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mobiles', to='phone.brand')),
            ],
            options={
                'verbose_name': 'mobile',
                'verbose_name_plural': 'mobiles',
                'ordering': ['brand', 'price'],
            },
        ),
    ]
