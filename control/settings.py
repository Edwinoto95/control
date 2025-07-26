import os
from pathlib import Path
import dj_database_url  # Asegúrate de tener dj-database-url instalado


# BASE_DIR apunta a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Clave secreta: deberías usar una variable de entorno en producción
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-temporal-para-desarrollo')


# DEBUG debe ser False en producción, con variable de entorno para configurarlo
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'  # Por defecto True si no está definido


# ALLOWED_HOSTS: se define con variable de entorno o con localhost para desarrollo
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost 127.0.0.1 192.168.100.150').split()


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Aplicaciones.gasto',  # Tu aplicación
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir estáticos con Gunicorn en Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLs principales del proyecto
ROOT_URLCONF = 'control.urls'


# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Plantillas personalizadas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = 'control.wsgi.application'


# Configuración de la base de datos usando dj_database_url para Render
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL', 'postgres://postgres:Danilo8669@localhost:5432/gasto'),
        conn_max_age=600,
        ssl_require=False  # Cambia a True si Render o tu BD usan SSL
    )
}


# Validadores de contraseña (dejar vacíos si quieres sin restricciones)
AUTH_PASSWORD_VALIDATORS = [
    # Puedes agregar validadores aquí si usas autenticación
]


# Configuración regional
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True


# Configuración de archivos estáticos

STATIC_URL = '/static/'

# Durante desarrollo puedes usar esta carpeta para estáticos locales
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'control/static'),
]

# Para producción, carpeta donde collectstatic recopila todos los archivos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise para servir archivos estáticos comprimidos y con cache
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Ajuste recomendado en Render para seguridad al servir estáticos
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Configuración por defecto para campos auto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

