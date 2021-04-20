# Generated by Django 3.1.4 on 2021-04-18 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0002_buku_jumlah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='buku',
            name='judul',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penerbit',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penulis',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='buku',
            name='kelompok',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perpus.kelompok'),
        ),
    ]
