# Generated by Django 3.1.5 on 2021-01-20 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210119_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='Capacity',
            new_name='no_bed',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='bed',
            new_name='no_guest',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='number',
            new_name='t_number',
        ),
        migrations.AddField(
            model_name='hotels',
            name='landmark',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='room',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.CreateModel(
            name='Room_categories',
            fields=[
                ('ca_id', models.AutoField(primary_key=True, serialize=False)),
                ('categorie', models.CharField(max_length=150)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.hotels')),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.room_categories'),
        ),
    ]