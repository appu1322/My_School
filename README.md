# My School

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/appu1322/My_School.git
$ cd My_School
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Intoduct

My school is an platform running by colleges. which provide student to get access into my school web application, where student can learn online during covid-19 pandemic. Which ensure thart not to breake in learning.

## Login

`http://127.0.0.1:8000/` . This is an home page where you have login for access cources. Login credentials are given in superuser_password.txt file.

### Admin Panel

To hanle full control of project you have login into admin panel uding url `http://127.0.0.1:8000/admin/login/?next=/admin/`. Credentials of login provided in superuser_password.txt file. 

### Add more users for login into courses

using url `http://127.0.0.1:8000/admin/login/?next=/admin/`. visit user table in admin panel and add more user by proving username and password.
