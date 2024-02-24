### Linting
https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/


### imports
[as per POP8](https://pep8.org/#imports)

### CSS styling in Django forms
https://stackoverflow.com/questions/5827590/css-styling-in-django-forms

### Multiple settings modules
Check this page [Django Tips #20 Working With Multiple Settings Modules](https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html) and (https://medium.com/@ayarshabeer/django-best-practice-settings-file-for-multiple-environments-6d71c6966ee2)
Note from Daniel: you will have to change the `wsgi.py` file so that Apache loads the production file.
Note from Daniel, it appears it does not work!!!

### Apache with WSGI
Need to install the Ubuntu packages
```bash
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```


### Activate the virtual environment
```bash
source </path/to/new/virtual/environment>/bin/activate
```


### Once a new Python package has been installed.
It is necessary to update the `requirements.txt` file.
```bash
pip freeze --all > requirements.txt
```
ensure you add the `--all` option.

### Development server
Within the Django root
```bash
python manage.py runserver 0.0.0.0:3000 --settings=myproject.settings --insecure
```

### Upgrade Bootstrap
* Download the Bootstrap distribution and the Source.
* Put the `assets` directory under `core/static/bootstrap/`
* Put the `dist` directory under `core/static/bootstrap/`
* Put the `examples` directory under `core/static/bootstrap/`
* Instruct Django to copy all the static files to the Django `static/` root. That is:
```bashsource
python manange.py collectstatic
```


### Git
* Create a new branch or use an existing development branch

    * To create a new branch
```bash
git checkout -b <new_branch_name>
```

    * To use an existing branch
```bash
git checkout <branch_name>https://www.markdownguide.org/extended-syntax
```

* Make the changes you want
* Add the changes
```bash
git add -A
```
* Commit the changes
```bash
git commit -m "<message"
```
