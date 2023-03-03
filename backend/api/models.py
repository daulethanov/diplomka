from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

SPECIAL = (
    ('МАТ', 'Математика'),
    ('ФИЗ', 'Физика'),
    ('ИНФ', 'Информатика'),
    ('ХИМ', 'Химия'),
    ('БИО', 'Биология'),
    ('ГЕО', 'География'),
    ('ИСТ', 'История'),
    ('ЛИН', 'Лингвистика'),
    ('ФИЛ', 'Философия'),
    ('СОЦ', 'Социология'),
    ('ЭКО', 'Экономика'),
    ('ПОЛ', 'Политология'),
    ('ПСИ', 'Психология'),
    ('ЮРИ', 'Юриспруденция'),
    ('МЕН', 'Менеджмент'),
    ('МАР', 'Маркетинг'),
    ('ФИН', 'Финансы'),
    ('КОМ', 'Компьютерные науки'),
    ('ЭЛЕ', 'Электроника'),
    ('АВТ', 'Автоматика'),
    ('МЕХ', 'Механика'),
    ('СТР', 'Строительство'),
    ('АРХ', 'Архитектура'),
    ('ДИЗ', 'Дизайн'),
    ('ИЗО', 'Изобразительное искусство'),
    ('МУЗ', 'Музыка'),
    ('ТЕА', 'Театральное искусство'),
    ('КИН', 'Кино и телевидение'),
    ('ЖУР', 'Журналистика'),
    ('РЕК', 'Реклама'),
    ('ПУБ', 'Паблик рилейшнз'),
    ('ТУР', 'Туризм'),
    ('ГОС', 'Государственное управление'),
    ('НКО', 'Некоммерческие организации'),
    ('МЕЖ', 'Международные отношения'),
    ('МЕД', 'Медицина'),
    ('ФАР', 'Фармация'),
    ('ВЕТ', 'Ветеринария'),
    ('ПЕД', 'Педагогика'),
    ('ФИЗК', 'Физическая культура'),
    ('ТЕХ', 'Технологии'),
    ('АГР', 'Агрономия'),
    ('ЛЕС', 'Лесное хозяйство'),
    ('РАД', 'Радиофизика'),
    ('АСТР', 'Астрономия'),
    ('ГЕОЛ', 'Геология'),
    ('МЕТ', 'Металлургия')
)


class University(models.Model):
    name = models.CharField(max_length=100, verbose_name='Университет')
    title = models.CharField(max_length=100, verbose_name='Микро описани')
    image = models.ImageField(upload_to='image', verbose_name='Картинка')
    email = models.EmailField(max_length=100, verbose_name='Почта', unique=True)
    contact_data = models.CharField(max_length=255, verbose_name='Контактные данные')
    description = models.TextField(verbose_name='Описание')
    special = models.CharField(choices=SPECIAL, verbose_name='Специальности', max_length=100)
    document = models.FileField(upload_to='document', verbose_name='Документ')

    class Meta:
        verbose_name = 'Универ'
        verbose_name_plural = 'Универы'


class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, email, password=None):
        if not email:
            raise ValueError("Error")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            first_name=first_name,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, email, password=None):
        user = self.create_user(
            first_name=first_name,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email', max_length=230, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    def __str__(self):
        return self.email
