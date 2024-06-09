from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=10, choices=[('customer', 'Заказчик'), ('employee', 'Сотрудник')],
                            default='customer')
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set'
    )

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=10, choices=[('standard', 'Стандартный'), ('extended', 'Расширенный')],default='standard')
    def __str__(self):
        return f"{self.user}"

TASK_STATUS_CHOICES = (
    ('PENDING', 'Ожидает исполнителя'),
    ('IN_PROGRESS', 'В процессе'),
    ('COMPLETED', 'Выполнена'),
)

class Task(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=TASK_STATUS_CHOICES, default='PENDING')
    report = models.TextField(blank=True, null=True)
    description = models.TextField(default='пусто')
    is_closed = models.BooleanField(default=False)
    def __str__(self):
        return f"Задача {self.id} от {self.customer}"
