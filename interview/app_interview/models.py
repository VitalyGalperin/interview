from django.db import models
from django.contrib.auth.models import User


class Interviews(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=400, verbose_name='описание')
    start_at = models.DateTimeField(auto_now_add=True, verbose_name='дата старта')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='дата окончания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Questions(models.Model):
    ANSWER_TYPE_CHOICES = [
        ('T', 'ответ текстом'),
        ('O', 'ответ с выбором одного варианта'),
        ('M', 'ответ с выбором нескольких вариантов'),
    ]

    Interview = models.ForeignKey(Interviews, on_delete=models.CASCADE, related_name='interview_link')
    answer_type = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES, verbose_name='тип вопроса')
    text = models.CharField(max_length=500, verbose_name='текст вопроса')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Options(models.Model):
    text = models.CharField(max_length=500, verbose_name='Вариант ответа')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_link')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_link')
    text_answer = models.CharField(max_length=500, null=True, blank=True, verbose_name='Текстовый ответ')
    choice_answer = models.ForeignKey(Options, null=True, blank=True, on_delete=models.CASCADE, related_name='option_link')

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'

