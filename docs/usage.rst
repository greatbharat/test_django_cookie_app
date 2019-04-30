=====
Usage
=====

To use test_django_cookie_app in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'test_django_cookie_app.apps.TestDjangoCookieAppConfig',
        ...
    )

Add test_django_cookie_app's URL patterns:

.. code-block:: python

    from test_django_cookie_app import urls as test_django_cookie_app_urls


    urlpatterns = [
        ...
        url(r'^', include(test_django_cookie_app_urls)),
        ...
    ]
