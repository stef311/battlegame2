# Generated by Django 2.0.2 on 2018-03-20 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servers', '0002_auto_20180320_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinateX', models.IntegerField()),
                ('coordinateY', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('tile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.Tile')),
                ('warrior1', models.IntegerField(default=0)),
                ('warrior2', models.IntegerField(default=0)),
                ('warrior3', models.IntegerField(default=0)),
                ('wood', models.IntegerField(default=0)),
                ('iron', models.IntegerField(default=0)),
                ('culture', models.IntegerField(default=0)),
                ('science', models.IntegerField(default=0)),
                ('silver', models.IntegerField(default=0)),
            ],
            bases=('places.tile',),
        ),
        migrations.AddField(
            model_name='tile',
            name='gameserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.GameServer'),
        ),
    ]
