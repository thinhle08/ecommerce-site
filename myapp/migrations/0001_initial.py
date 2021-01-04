# Generated by Django 3.1.2 on 2020-11-17 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('keyword', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('size', models.TextField()),
                ('image', models.FileField(upload_to='documents/')),
                ('status', models.BooleanField(default=True)),
                ('active_home', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('keyword', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='myapp.category')),
            ],
        ),
    ]