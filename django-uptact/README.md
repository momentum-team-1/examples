# Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- There is a custom user model defined in `users.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Poetry](https://python-poetry.org/) is used to manage dependencies.

## Using this template

In an empty directory, run:

```
django-admin startproject --template=https://github.com/momentumlearn/django-project-template/archive/master.zip <your_project_name> .
cp <your_project_name>/.env.sample <your_project_name>/.env
poetry install
poetry shell
./manage.py migrate
```

Remember to change `<your_project_name>` to your actual project name. You must have `django` and `poetry` installed in your system Python for this to work.
