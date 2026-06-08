from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)  # Soft delete

    def __str__(self):
        return self.email

class Resource(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., 'projects', 'tasks', 'users'
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., 'view', 'create', 'update', 'delete', 'list'
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)  # admin, manager, employee
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    allowed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('role', 'resource', 'action')

    def __str__(self):
        return f"{self.role} | {self.action} on {self.resource} ({'allowed' if self.allowed else 'denied'})"

class UserRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')