# Generated by Django 4.0.4 on 2023-01-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atype', models.CharField(choices=[('A', 'Admin'), ('P', 'Pacjent'), ('L', 'Lekarz')], max_length=200)),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('addrs', models.CharField(max_length=50)),
                ('postc', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('pass1', models.CharField(max_length=50)),
                ('pass2', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
