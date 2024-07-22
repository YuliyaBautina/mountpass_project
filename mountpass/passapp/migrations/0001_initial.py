# Generated by Django 5.0.6 on 2024-07-05 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('1А', '1А'), ('2А', '2А'), ('3А', '3А'), ('1B', '1Б'), ('2B', '2Б'), ('3B', '3Б'), ('3B*', '3Б*')], max_length=3, null=True)),
                ('summer', models.CharField(blank=True, choices=[('1А', '1А'), ('2А', '2А'), ('3А', '3А'), ('1B', '1Б'), ('2B', '2Б'), ('3B', '3Б'), ('3B*', '3Б*')], max_length=3, null=True)),
                ('autumn', models.CharField(blank=True, choices=[('1А', '1А'), ('2А', '2А'), ('3А', '3А'), ('1B', '1Б'), ('2B', '2Б'), ('3B', '3Б'), ('3B*', '3Б*')], max_length=3, null=True)),
                ('spring', models.CharField(blank=True, choices=[('1А', '1А'), ('2А', '2А'), ('3А', '3А'), ('1B', '1Б'), ('2B', '2Б'), ('3B', '3Б'), ('3B*', '3Б*')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('fam', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('otc', models.CharField(max_length=128)),
                ('phone', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(default='пер.', max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('other_titles', models.CharField(max_length=128)),
                ('connect', models.CharField(max_length=128)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NW', 'New'), ('PN', 'Pending'), ('AC', 'Accepted'), ('RJ', 'Rejected')], default='NEW', max_length=2)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='passapp.myuser')),
                ('coord_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coords', to='passapp.coord')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='passapp.level')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mountpass/')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='passapp.perevaladded')),
            ],
        ),
    ]
