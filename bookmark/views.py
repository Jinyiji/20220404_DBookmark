from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    # bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']            # '__all__'
    template_name_suffix = '_create'    # bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']    # '__all__'
    template_name_suffix = '_update'    # bookmark_update.html
    success_url = reverse_lazy('bookmark:list')