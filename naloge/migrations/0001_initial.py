# Generated by Django 4.2.7 on 2023-11-20 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('konzola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_points', models.IntegerField()),
                ('category', models.CharField(choices=[('nnz', 'Nič ne znam'), ('obv', 'obvladam')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('points', models.IntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naloge.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konzola.user')),
            ],
        ),
    ]
