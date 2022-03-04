from django.contrib import admin

from proba_strzelnicza import models

admin.site.register(models.Bullet)
admin.site.register(models.Weapon)
admin.site.register(models.Factor)
admin.site.register(models.Material)
admin.site.register(models.Base)
admin.site.register(models.Shot)
admin.site.register(models.Ricochet)
