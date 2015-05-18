import os
from django.conf import settings

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
        {
            'theme': "modern",
            'relative_urls': False,
            'plugins': ['advlist autolink lists link image charmap print preview anchor',
                        'searchreplace visualblocks code fullscreen',
                        'insertdatetime media table contextmenu paste textcolor'],
            'toolbar1': 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent',
            'toolbar2': 'forecolor backcolor | link image'
        })

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL',os.path.join(settings.STATIC_URL, 'tiny_mce/tinymce.min.js'))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT',os.path.join(settings.STATIC_ROOT, 'tiny_mce'))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL','%sjs/tiny_mce/tinymce.min.js' % settings.MEDIA_URL)
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]