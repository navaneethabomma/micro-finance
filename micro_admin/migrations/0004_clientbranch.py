# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 06:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('micro_admin', '0003_auto_20160706_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_on', models.DateField(auto_now=True)),
                ('changed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='changed_by', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_name', to='micro_admin.Client')),
                ('from_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_branch', to='micro_admin.Branch')),
                ('to_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_branch', to='micro_admin.Branch')),
            ],
        ),
    ]