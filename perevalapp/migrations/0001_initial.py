# Generated by Django 4.2.7 on 2023-11-13 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fam', models.CharField(default='', max_length=100, verbose_name='Фамилия')),
                ('user_name', models.CharField(default='', max_length=100, verbose_name='Имя')),
                ('user_otc', models.CharField(default='', max_length=100, verbose_name='Отчество')),
                ('user_phone', models.CharField(default='', max_length=20, verbose_name='Тел.')),
                ('user_email', models.CharField(default='', max_length=50, unique=True, verbose_name='Почта')),
            ],
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Ширина')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности перевала',
                'verbose_name_plural': 'Уровни сложности перевала',
            },
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(default=None, max_length=255, verbose_name='Общее название')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название горы')),
                ('other_titles', models.CharField(max_length=255, verbose_name='Альтернативное название горы')),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NEW', 'Новая информация'), ('ACCEPTED', 'Информация принята'), ('PENDING', 'В процессе'), ('REJECTED', 'Информация отклонена')], default='NEW', max_length=10)),
                ('coord_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.coords')),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.level')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.authors')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('data', models.URLField(blank=True, null=True, verbose_name='Изображение')),
                ('pereval_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='perevalapp.pereval')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]