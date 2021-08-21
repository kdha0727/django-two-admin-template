# Django Boiler Plate for Two-Factor Admin Site
> You can easily create django project which requires two or multi admin sites.

Setup
``` bash
$ python -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

# Features

## Two Admin Site

In [`admin_site.sites`](./admin_site/sites/) package, there exist two admin site modules ([`site_superuser.py`](./admin_site/sites/site_superuser.py) and [`site_teacher.py`](./admin_site/sites/site_teacher.py)).

1. site_superuser

This is an original admin site object, but only superuser can log-in with / enter this site. (`user.is_superuser == True`) You can add extra conditions to this superuser-only admin site.

2. site_teacher

This is an admin site object constructed from new class, which makes superuser unable to log-in with this site. Staffs (`user.is_superuser == False` but `user.is_staff == True`) can log-in with this site.

## Separated settings file

1. Local (Dev) Environment

In Windows or MacOS, django will serve for default debug settings automatically:
```
$ python manage.py runserver
```

2. Production Environment

In Linux, wsgi will serve with production settings, depending on the `secret.json` file.

`secret.json` file should contain `ALLOWED_HOSTS`, `SECRET_KEY`, and `DATABASES` information like below:
```
{
  "ALLOWED_HOSTS": [
    "your host ip or domains"
  ],
  "SECRET_KEY" : "production secret key",
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.mysql",
      "NAME": "production database name",
      "USER": "production database user",
      "PASSWORD": "production database password",
      "HOST": "production database host",
      "PORT": "3306"
    }
  }
}
```

After configuring `secret.json`, run gunicorn with `config.wsgi:application` and have fun~


