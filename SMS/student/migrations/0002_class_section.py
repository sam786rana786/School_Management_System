# Generated by Django 2.0.3 on 2018-04-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('class_details', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('class_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('section', models.CharField(default='A', max_length=5)),
                ('classes', models.ForeignKey(db_column='class_name', on_delete=django.db.models.deletion.CASCADE, to='student.Class')),
            ],
        ),
    ]
