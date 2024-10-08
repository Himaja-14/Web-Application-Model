# Generated by Django 5.0.6 on 2024-07-07 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cand_id', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('orgname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HRadministrator.organization')),
            ],
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deptname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HRadministrator.department')),
                ('orgname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HRadministrator.organization')),
            ],
        ),
        migrations.CreateModel(
            name='requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisition_id', models.CharField(max_length=100, unique=True)),
                ('no_of_openings', models.IntegerField(default=0)),
                ('min_salary', models.IntegerField(null=True)),
                ('max_salary', models.IntegerField(null=True)),
                ('min_experiance', models.IntegerField(null=True)),
                ('max_experiance', models.IntegerField(null=True)),
                ('qualification', models.CharField(max_length=50, null=True)),
                ('positionname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HRadministrator.position')),
            ],
        ),
        migrations.CreateModel(
            name='requisition_candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HRadministrator.candidate')),
                ('requisition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HRadministrator.requisition')),
            ],
        ),
    ]
