# Generated by Django 3.1 on 2020-09-21 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200918_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글',
                'db_table': 'board',
            },
        ),
    ]
