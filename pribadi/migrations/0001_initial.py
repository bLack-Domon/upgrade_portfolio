# Generated by Django 4.2.4 on 2023-08-26 14:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=250, null=True)),
                ('isi_aplikasi', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('foto_aplikasi', models.ImageField(blank=True, max_length=250, null=True, upload_to='')),
                ('penulis', models.CharField(blank=True, max_length=250, null=True)),
                ('link_projek', models.CharField(blank=True, max_length=250, null=True)),
                ('tanggal', models.DateField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Galeri Aplikasi',
            },
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=250, null=True)),
                ('tentang_diri', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, max_length=250, null=True, upload_to='')),
                ('hp', models.CharField(blank=True, max_length=250, null=True)),
                ('fb', models.CharField(blank=True, max_length=250, null=True)),
                ('ig', models.CharField(blank=True, max_length=250, null=True)),
                ('github', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Profil Diri',
            },
        ),
    ]
