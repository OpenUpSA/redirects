Code4SA Redirects App
=====================

Redirects for Code4SA using [django-sky-redirects](https://github.com/concentricsky/django-sky-redirects).

Edit redirects at http://redirects.code4sa.org/admin/

Production deployment
---------------------

Production deployment assumes you're running on Heroku.

You will need:

* a django secret key
* a New Relic license key
* a cool app name

Create the app on dokku

Set configs:

```bash
dokku config:set redirects DJANGO_DEBUG=false \
                  DJANGO_SECRET_KEY=some-secret-key \
                  NEW_RELIC_APP_NAME=cool app name \
                  NEW_RELIC_LICENSE_KEY=new relic license key

git remote add dokku dokku@dokku.code4sa.org:<app_name>
git push dokku

dokku run <app_name> python manage.py migrate
dokku run <app_name> python manage.py createsuperuser
```

License
-------

MIT License
