# Import admin stuffs
from django.contrib import admin

# Import for making custom UserAdmin
from django.contrib.admin.forms import AdminAuthenticationForm as AuthForm
from django.contrib.auth.models import User
from common.forms import build_superuser_block_auth_form as build

# from ..admin_classes import TeacherUserAdmin


site_teacher = type('TeacherSite', (admin.sites.AdminSite, ), {'login_form': build(AuthForm)})(name='teacher')
# site_teacher.register(User, TeacherUserAdmin)  # todo: enable this feature before commit
site_teacher.enable_nav_sidebar = False
site_teacher.site_title = '{site-title}'
site_teacher.site_header = '{site-description}'
site_teacher.index_title = '{site-index}'


__all__ = ['site_teacher']
