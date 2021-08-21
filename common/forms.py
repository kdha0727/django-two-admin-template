from django.contrib.auth.forms import AuthenticationForm


def build_superuser_block_auth_form(base=AuthenticationForm):
    def confirm_login_allowed(self, user):
        base.confirm_login_allowed(self, user)
        if user.is_superuser:
            raise self.get_invalid_login_error()
    assert issubclass(base, AuthenticationForm)
    return type(
        'NonSuperuserAuthForm',
        (base, ),
        {'confirm_login_allowed': confirm_login_allowed}
    )
