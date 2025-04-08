# Generated by Django 5.1.5 on 2025-02-25 08:16

import apps.common.models.fields
import apps.common.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="o'zgartrilgan sana")),
                ('active', apps.common.models.fields.ActiveField(default=False, verbose_name='aktiv')),
                ('title', models.CharField(max_length=512, verbose_name='sarlavhasi')),
                ('title_uz', models.CharField(max_length=512, null=True, verbose_name='sarlavhasi')),
                ('title_ru', models.CharField(max_length=512, null=True, verbose_name='sarlavhasi')),
                ('title_en', models.CharField(max_length=512, null=True, verbose_name='sarlavhasi')),
                ('icon', models.FileField(upload_to=apps.common.utils.generate_upload_path, verbose_name='belgisi(.svg)')),
                ('count', models.PositiveBigIntegerField(default=0, verbose_name='statistika qiymati')),
                ('order', apps.common.models.fields.OrderField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='tartibi')),
            ],
            options={
                'verbose_name': 'Xayriya statistikasi ',
                'verbose_name_plural': '2. Xayriya statistikasi',
                'ordering': ('order',),
            },
        ),
        migrations.DeleteModel(
            name='PayStatictic',
        ),
        migrations.AddField(
            model_name='bannermenu',
            name='short_description_en',
            field=models.CharField(max_length=63, null=True, verbose_name='Menu haqida qisqacha'),
        ),
        migrations.AddField(
            model_name='bannermenu',
            name='short_description_ru',
            field=models.CharField(max_length=63, null=True, verbose_name='Menu haqida qisqacha'),
        ),
        migrations.AddField(
            model_name='bannermenu',
            name='short_description_uz',
            field=models.CharField(max_length=63, null=True, verbose_name='Menu haqida qisqacha'),
        ),
        migrations.AddField(
            model_name='bannermenu',
            name='title_en',
            field=models.CharField(max_length=31, null=True, unique=True, verbose_name='Menyu nomi'),
        ),
        migrations.AddField(
            model_name='bannermenu',
            name='title_ru',
            field=models.CharField(max_length=31, null=True, unique=True, verbose_name='Menyu nomi'),
        ),
        migrations.AddField(
            model_name='bannermenu',
            name='title_uz',
            field=models.CharField(max_length=31, null=True, unique=True, verbose_name='Menyu nomi'),
        ),
        migrations.AddField(
            model_name='charityproject',
            name='description_en',
            field=models.TextField(max_length=512, null=True, verbose_name='batafsil'),
        ),
        migrations.AddField(
            model_name='charityproject',
            name='description_ru',
            field=models.TextField(max_length=512, null=True, verbose_name='batafsil'),
        ),
        migrations.AddField(
            model_name='charityproject',
            name='description_uz',
            field=models.TextField(max_length=512, null=True, verbose_name='batafsil'),
        ),
        migrations.AddField(
            model_name='charityproject',
            name='title_en',
            field=models.CharField(max_length=256, null=True, unique=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='charityproject',
            name='title_ru',
            field=models.CharField(max_length=256, null=True, unique=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='charityproject',
            name='title_uz',
            field=models.CharField(max_length=256, null=True, unique=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='headermenu',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Menyu nomi'),
        ),
        migrations.AddField(
            model_name='headermenu',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Menyu nomi'),
        ),
        migrations.AddField(
            model_name='headermenu',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Menyu nomi'),
        ),
        migrations.AddField(
            model_name='musofirdonation',
            name='note_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Eslatma'),
        ),
        migrations.AddField(
            model_name='musofirdonation',
            name='note_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Eslatma'),
        ),
        migrations.AddField(
            model_name='musofirdonation',
            name='note_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Eslatma'),
        ),
        migrations.AddField(
            model_name='quote',
            name='full_name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='quote',
            name='full_name_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='quote',
            name='full_name_uz',
            field=models.CharField(max_length=256, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='quote',
            name='job_en',
            field=models.CharField(max_length=256, null=True, verbose_name='kasbi'),
        ),
        migrations.AddField(
            model_name='quote',
            name='job_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='kasbi'),
        ),
        migrations.AddField(
            model_name='quote',
            name='job_uz',
            field=models.CharField(max_length=256, null=True, verbose_name='kasbi'),
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_en',
            field=models.TextField(null=True, verbose_name='iqtibos'),
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_ru',
            field=models.TextField(null=True, verbose_name='iqtibos'),
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_uz',
            field=models.TextField(null=True, verbose_name='iqtibos'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_en',
            field=models.CharField(max_length=512, null=True, verbose_name='tavsifi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_ru',
            field=models.CharField(max_length=512, null=True, verbose_name='tavsifi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_uz',
            field=models.CharField(max_length=512, null=True, verbose_name='tavsifi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.CharField(max_length=512, null=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_ru',
            field=models.CharField(max_length=512, null=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_uz',
            field=models.CharField(max_length=512, null=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='usefullink',
            name='title_en',
            field=models.CharField(max_length=256, null=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='usefullink',
            name='title_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='sarlavhasi'),
        ),
        migrations.AddField(
            model_name='usefullink',
            name='title_uz',
            field=models.CharField(max_length=256, null=True, verbose_name='sarlavhasi'),
        ),
    ]
