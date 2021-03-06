# Generated by Django 3.2.5 on 2021-08-18 20:25

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('multifile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='website.multifile')),
                ('multiimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.multiimage')),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Text')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('cover_photo', models.ImageField(upload_to='news_images/', verbose_name='Imagine')),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
            bases=('website.multiimage', 'website.multifile'),
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
