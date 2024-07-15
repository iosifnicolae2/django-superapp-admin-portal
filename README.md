### django-superapp-admin-portal

### Getting started
```bash
pipx install django_superapp
django_superapp bootstrap-project \
        --template-repo https://github.com/django-superapp/django-superapp-default-project \
        ./my_superapp;
cd my_superapp;
cd superapp/apps;
django_superapp bootstrap-app \
    --template-repo https://github.com/django-superapp/django-superapp-admin-portal \
    ./my_superapp;
make setup-sample-env
make start-docker
```
### Documentation
For a more detailed documentation, visit [https://django-superapp.bringes.io](https://django-superapp.bringes.io).

