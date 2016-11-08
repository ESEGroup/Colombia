from django.contrib import admin
from .models import Funcionario, ChefeDeDepartamento, Recurso, Agendamento
# Register your models here.
admin.site.register(Funcionario)
admin.site.register(ChefeDeDepartamento)
admin.site.register(Recurso)
admin.site.register(Agendamento)