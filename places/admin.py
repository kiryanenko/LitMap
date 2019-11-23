from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from places.forms import PlacePushForm
from places.models import Tag, Place


def place_action(self, request, users_qs, *args, **kwargs):
    form = None
    if 'apply' in request.POST:
        form = PlacePushForm(users_qs, request.POST)
        if form.is_valid():
            form.save()
            push_msg = 'Рассылка будет выполнена в фоне'
            self.message_user(request, push_msg)
            return HttpResponseRedirect(reverse('admin:core_user_changelist'))

    if form is None:
        is_all_selected = self.action_form(request.POST.copy()).data['select_across']
        form = PlacePushForm(users_qs, initial={
            '_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME),
            'select_across': is_all_selected,
        })

    context = {
        'form': form,
        'title': 'Пуш уведомления о местах',
        'opts': self.model._meta,
        'current_action': request.POST['action'],
    }
    return render(request, 'admin/places/place_push.html', context)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_text')

