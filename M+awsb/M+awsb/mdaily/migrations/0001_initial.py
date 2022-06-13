# Generated by Django 4.0 on 2022-06-10 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MOrg',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False, unique=True)),
                ('org_id', models.CharField(db_column='org_id', default='', max_length=64)),
                ('name', models.CharField(max_length=12)),
                ('showas', models.CharField(max_length=128, null=True)),
                ('repid', models.IntegerField(db_column='repID')),
            ],
            options={
                'verbose_name_plural': 'M+Orgs',
                'db_table': 'M+_orgs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MSub',
            fields=[
                ('name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=12)),
                ('note', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'M+Subscriptions',
                'db_table': 'M+_sub',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MInv',
            fields=[
                ('inv_id', models.SmallAutoField(db_column='inv_id', primary_key=True, serialize=False)),
                ('sin', models.CharField(max_length=8)),
                ('dated', models.DateField()),
                ('sub_start', models.DateField(null=True)),
                ('sub_duration', models.IntegerField(default=6)),
                ('sub_end', models.DateField(null=True)),
                ('sub_active_rate', models.FloatField()),
                ('sub_dorm_rate', models.FloatField()),
                ('sub_type', models.ForeignKey(db_column='sub_type', default='ELIOT6', on_delete=django.db.models.deletion.CASCADE, to='mdaily.msub')),
            ],
            options={
                'verbose_name_plural': 'M+Invoices',
                'db_table': 'M+_inv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MDevOwn',
            fields=[
                ('imei', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('inv_id', models.ForeignKey(db_column='inv_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='mdaily.minv')),
                ('owner', models.ForeignKey(db_column='owner', on_delete=django.db.models.deletion.DO_NOTHING, to='mdaily.morg')),
            ],
            options={
                'verbose_name_plural': 'M+DeviceOwners',
                'db_table': 'M+_dev_own',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MDaily',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('imei', models.BigIntegerField()),
                ('checked_on', models.DateTimeField()),
                ('last_measure_at', models.DateTimeField(blank=True, null=True)),
                ('count', models.SmallIntegerField()),
                ('org', models.ForeignKey(db_column='org', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mdaily.morg')),
            ],
            options={
                'verbose_name_plural': 'M+DailyMeasures',
                'db_table': 'M+_daily',
                'managed': True,
            },
        ),
    ]