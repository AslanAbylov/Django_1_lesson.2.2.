# from django.db import models
# from django.contrib.auth.models import User
#
#
#
# class CustomUser(User):
#     class Meta:
#         verbose_name = 'Пользователи'
#         verbose_name_plural = 'Пользователи'
#     ADMIN = 1
#     VIPClient = 2
#     CLIENT = 3
#     USER_TYPE = (
#         (ADMIN, 'ADMIN'),
#         (VIPClient, 'VIP-Client')
#         (CLIENT, 'CLIENT')
#     )
#     MALE = 1
#     FEMALE = 2
#     OTHER = 3
#     GENDER_TYPE = (
#         (MALE, 'MALE'),
#         (FEMALE, 'FEMALE'),
#         (OTHER, 'OTHER')
#     )
#     user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользавателя', default=CLIENT)
#     phone_number = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Гендер')

