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
   4. bookmark/views BookmarkListView
   5. bookmark/urls bookmark:list
   6. templates bookmark_list.html
   7. bookmark/views BookmarkCreateView
   8. urls, bookmark/urls bookmark:add
   9. templates bookmark_create.html
   10. bookmark/views BookmarkDetailView
   11. bookmark/urls bookmark:detail
   12. templates bookmark_detail.html
   13. bookmark/views BookmarkUpdateView
   14. bookmark/urls bookmark:edit
   15. templates bookmark_update.html
   16. get_absolute_url() in Bookmark
   17. bookmark/views BookmarkDeleteView
   18. bookmark/urls bookmark:delete
   19. templates bookmark_confirm_delete.html
4. 🧨🎇 기능 완성 🎇
   1. templates/base.html, extends 'base.html', block title, content