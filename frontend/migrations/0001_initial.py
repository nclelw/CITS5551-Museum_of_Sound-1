# Generated by Django 2.1 on 2020-05-07 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_title', models.TextField()),
                ('prod_description', models.TextField(default='')),
                ('upload_time', models.DateTimeField()),
                ('audio_file', models.FileField(upload_to='')),
                ('is_approved', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='N', max_length=256)),
                ('uploader_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSound',
            fields=[
                ('sound_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_file', models.FileField(null=True, upload_to='')),
                ('title', models.CharField(default='', max_length=50)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('audio_file', models.FileField(upload_to='')),
                ('is_approved', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='N', max_length=3)),
                ('is_tagged', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
