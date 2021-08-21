# Import admin stuffs
from django.contrib import admin

from .sites import site_superuser, site_teacher


# Define register function (function that registers model in both site)

def register(*models, admin_class=None):
    if admin_class is None:
        # Return decorator
        def decorator(cls):
            teacher_wrapper = admin.register(*models, site=site_teacher)
            superuser_wrapper = admin.register(*models, site=site_superuser)
            return teacher_wrapper(superuser_wrapper(cls))
        return decorator
    else:
        # Register models with admin class in both site
        site_teacher.register(models, admin_class)
        site_superuser.register(models, admin_class)


__all__ = ['site_superuser', 'site_teacher', 'register']
