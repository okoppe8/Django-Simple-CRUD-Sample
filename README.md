Django-Simple-CRUD-Sample
====

Overview

## Description

Djangoのチュートリアル用サンプルアプリケーションです。
紹介記事：[[Python] Djangoチュートリアル - 汎用業務Webアプリを最速で作る](https://qiita.com/okoppe8/items/54eb105c9c94c0960f14)

## Version

Django 2.0.2

## Usage

Windows Command Prompt

```
cd Django-Simple-CRUD-Sample
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py createsuperuser 
manage.py runserver
```

Open URL http://localhost:8000
