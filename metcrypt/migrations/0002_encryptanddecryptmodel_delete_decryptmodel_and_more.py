# Generated by Django 4.0.2 on 2022-02-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metcrypt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptAndDecryptModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('result', models.TextField()),
                ('what_type', models.CharField(choices=[('c', 'caesar'), ('r', 'rot16')], max_length=1)),
                ('encordec', models.CharField(choices=[('e', 'encrypt'), ('d', 'decrypt')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DecryptModel',
        ),
        migrations.DeleteModel(
            name='EncryptModel',
        ),
    ]
