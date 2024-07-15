from django.urls import reverse_lazy
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _

def extend_superapp_settings(main_settings):
    main_settings['INSTALLED_APPS'] = [
        'admin_confirm',
        'unfold',
        "unfold.contrib.filters",
        "unfold.contrib.import_export",
        "unfold.contrib.guardian",
        "unfold.contrib.simple_history",
        "unfold.contrib.forms",
        'superapp.apps.admin_portal',
    ] + main_settings['INSTALLED_APPS'] + [
        "debug_toolbar",
        "import_export",
    ]
    main_settings.update({
        'LOGIN_URL': "admin:login",
        'LOGIN_REDIRECT_URL': reverse_lazy("admin:index"),
    })

    main_settings['UNFOLD'] = {
        "SITE_HEADER": _("SuperApp Demo"),
        "SITE_TITLE": _("SuperApp Demo"),
        "SITE_SYMBOL": "settings",
        "SHOW_HISTORY": False,
        "STYLES": [],
        "SCRIPTS": [
            lambda request: static("js/apex.min.js"),
            lambda request: static("js/flowbite.min.js"),
            lambda request: static("js/jquery-3.7.1.min.js"),
            lambda request: static("js/modals.js"),
        ],
    }
