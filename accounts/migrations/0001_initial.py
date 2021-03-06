# Generated by Django 3.0 on 2021-02-11 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(max_length=500, upload_to='media/images/profile_picture')),
                ('bio', models.TextField()),
                ('website', models.URLField(blank=True)),
                ('gitlab_url', models.URLField(blank=True)),
                ('behance_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('followers', models.ManyToManyField(related_name='followed_by', to='accounts.Profile')),
                ('following', models.ManyToManyField(to='accounts.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GitHubRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('top_language', models.CharField(blank=True, max_length=255)),
                ('stars', models.IntegerField(blank=True)),
                ('fork', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GitHubProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repos', models.ManyToManyField(to='accounts.GitHubRepo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
