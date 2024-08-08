from django.db import models
from apps.users.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователи", related_name="user_task")
    title = models.CharField(max_length=155, verbose_name="Заголовок для таска")
    description = models.TextField(verbose_name="Описание для таска")
    completed = models.BooleanField(default=False, verbose_name="Статус задачи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания задачи")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"