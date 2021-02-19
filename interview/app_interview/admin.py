from django.contrib import admin
from .models import *


@admin.register(Interviews)
class InterviewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_at', 'finish_at')


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('Interview', 'answer_type', 'text')


@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('user', 'anon_user', 'question', 'text_answer', 'choice_answer')

