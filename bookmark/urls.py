from django.urls import path

from bookmark.views import BookmarkListView

app_name = 'bookmark'

urlpatterns = [
    path('list/', BookmarkListView.as_view(), name='list')  # bookmark:list
]