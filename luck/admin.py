from django.contrib import admin

from luck.models import ModelRomanova
import inspect
import luck.models


ms = inspect.getmembers(luck.models, inspect.isclass)
for model in ms: admin.site.register(model[1])

# Register your models here.
