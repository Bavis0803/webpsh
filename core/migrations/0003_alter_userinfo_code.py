# Generated by Django 4.2.9 on 2024-03-03 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_codeinfo_table_alter_userinfo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.codeinfo'),
        ),
    ]
