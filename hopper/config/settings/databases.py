from configurations import values


class PostgreSQLDatabases(object):
    """Settings for local PostgreSQL databases."""
    DATABASES = values.DictValue({
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'hopper',
            'USER': 'hopper',
            'PASSWORD': 'hopper',
            'HOST': 'localhost',
            'CONN_MAX_AGE': None,
        },
    })


class EmptyDatabases(object):
    """Empty databases settings, used to force to overwrite them."""
    DATABASES = values.DictValue({
        'default': {
            'ENGINE': '',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
        },
    })
