# DBookmark
- project/urls.py -> app/urls.py -> views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트
- 개발 순서 : models.py, views.py, urls.py, templates
1. startproject DBookmark
   1. python -m pip install django~=3.2
   2. django-admin startproject DBookmark .
   3. python manage.py runserver
2. startapp bookmark
   1. python manage.py startapp bookmark
   2. add 'bookmark', to INSTALLED_APPS in settings.py
3. bookmark/models Bookmark
   1. python manage.py makemigrations bookmark
      1. models -> DB로 옮기기 위한 py
   2. python manage.py migrate
      1. DB 테이블 만들기
   3. bookmark/admin Bookmark
      1. python manage.py createsuperuser
      2. bookmark/models Bookmark \_\_str\_\_()