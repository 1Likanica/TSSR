from django.db import models

""" пользователи - авторы сообщений о географических объектах """
class Authors(models.Model):
    user_fam = models.CharField('Фамилия', max_length=100, default='')   # - пользователь - фамилия
    user_name = models.CharField('Имя', max_length=100, default='')      # - пользователь - имя
    user_otc = models.CharField('Отчество', max_length=100, default='')  # - пользователь - отчество
    user_phone = models.CharField('Тел.', max_length=20, default='')     # - пользователь - номер телефона
    user_email = models.CharField('Почта', max_length=50, default='')   # - пользователь - почта

    def __str__(self):
        return f'{self.user_fam} {self.user_name[0]}. {self.user_otc[0]}.'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'


"""  координаты гео-объекта """
class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Ширина')    # - ширина
    longitude = models.FloatField(verbose_name='Долгота')  # - долгота
    height = models.IntegerField('Высота')                 # - высота

    def __str__(self):
        return f'{self.latitude}°, {self.longitude}°, {self.height}м'

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


LEVEL = [
    ('1a', '1A'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('4a', '4А'),
    ('4b', '4Б'),
    ('5a', '5А'),
    ('5b', '5Б'),
]

""" Уровни сложности в различные времена года """
class Level(models.Model):
    # категория трудности - зимой
    winter = models.CharField(max_length=2, choices=LEVEL, verbose_name='Зима', null=True, blank=True, )
    # категория трудности - летом
    summer = models.CharField(max_length=2, choices=LEVEL, verbose_name='Лето', null=True, blank=True, )
    # категория трудности - осенью
    autumn = models.CharField(max_length=2, choices=LEVEL, verbose_name='Осень', null=True, blank=True, )
    # категория трудности - весной
    spring = models.CharField(max_length=2, choices=LEVEL, verbose_name='Весна', null=True, blank=True, )

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = 'Уровень сложности перевала'
        verbose_name_plural = 'Уровни сложности перевала'


""" информация о географических объектах, полученная от пользователей """
class Pereval(models.Model):
    NEW = 'NEW'
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    STATUS_CHOICES = (
        ('NEW', 'Новая информация'),
        ('ACCEPTED', 'Информация принята'),
        ('PENDING', 'В процессе'),
        ('REJECTED', 'Информация отклонена'),
    )
    beauty_title = models.CharField(max_length=255, verbose_name='Вид объекта', default=None)  # - вид объекта (
    # например: перевал, ущелье, расщелина)
    title = models.CharField(max_length=255, verbose_name='Название горы')  # - наименование # объекта
    # - другие наименования объекта
    other_titles = models.CharField(max_length=255, verbose_name='Альтернативное название горы', null=True, blank=True)
    connect = models.TextField(null=True, blank=True, verbose_name='Соединение')
    add_time = models.DateTimeField(auto_now_add=True)  # - дата и время создания
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW, verbose_name='Статус')
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE, verbose_name='Координаты')  # координаты
    # гео-объекта
    user_id = models.ForeignKey(Authors, on_delete=models.CASCADE, verbose_name='Автор')  # пользователь
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Уровень сложности')

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'


""" фотографии гео-объекта """
class Images(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    data = models.URLField(verbose_name='Изображение', null=True, blank=True)
    pereval_id = models.ForeignKey(Pereval, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'

