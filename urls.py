from django.urls import path

def extend_superapp_urlpatterns(main_urlpatterns):
    from .sites import superapp_admin_site
    main_urlpatterns += [
        path("portal/", superapp_admin_site.urls),
    ]


def extend_superapp_admin_urlpatterns(main_admin_urlpatterns):
    main_admin_urlpatterns += [
    ]
