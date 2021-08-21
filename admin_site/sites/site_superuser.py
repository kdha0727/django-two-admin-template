# Import admin stuffs
from django.contrib import admin

# Import for making custom UserAdmin
import types


site_superuser = admin.site  # Already constructed
site_superuser.has_permission = types.MethodType(
    lambda self, request: request.user.is_superuser,
    site_superuser
)
# site_superuser.unregister(User)
# site_superuser.register(User, SuperuserUserAdmin)  # todo: enable this feature before commit
site_superuser.enable_nav_sidebar = False
site_superuser.site_title = '{site-title}'
site_superuser.site_header = '{site-description}'
site_superuser.index_title = '{site-index}'


__all__ = ['site_superuser']
