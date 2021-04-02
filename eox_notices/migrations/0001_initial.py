# Generated by Django 3.1.7 on 2021-04-02 01:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0004_initial_part_4'),
    ]

    operations = [
        migrations.CreateModel(
            name='EoxNotice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('end_of_sale', models.DateField(blank=True, null=True)),
                ('end_of_support', models.DateField(blank=True, null=True)),
                ('end_of_sw_releases', models.DateField(blank=True, null=True)),
                ('end_of_security_patches', models.DateField(blank=True, null=True)),
                ('notice_url', models.URLField(blank=True)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcim.devicetype')),
                ('devices', models.ManyToManyField(to='dcim.Device')),
            ],
            options={
                'ordering': ('end_of_support', 'end_of_sale'),
            },
        ),
        migrations.AddConstraint(
            model_name='eoxnotice',
            constraint=models.UniqueConstraint(fields=('device_type',), name='unique_device_type'),
        ),
    ]
