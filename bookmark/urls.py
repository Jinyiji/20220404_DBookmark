from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView

app_name = 'bookmark'

urlpatterns = [
    path('list/', BookmarkListView.as_view(), name='list'),  # bookmark:list
    path('add/', BookmarkCreateView.as_view(), name='add'),  # bookmark:add
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),  # bookmark:detail
]