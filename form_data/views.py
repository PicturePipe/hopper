from braces.views import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from rest_framework.authtoken.models import Token

from .forms import FormDataCreateForm
from . import models


class FormDataCreateView(LoginRequiredMixin, generic.FormView):
    form_class = FormDataCreateForm
    success_url = reverse_lazy('form_data_list')
    template_name = 'form_data/formdata_create_view.html'

    def form_valid(self, form):
        models.FormData.objects.create(author=self.request.user, title=form.cleaned_data['title'])
        return redirect(self.get_success_url())


class FormDataUpdateView(generic.DetailView):
    template_name = 'form_data/formdata_update_view.html'
    model = models.FormData

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied()
        return super(FormDataUpdateView, self).dispatch(request, *args, **kwargs)

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        return token.key


class FormDataListView(LoginRequiredMixin, generic.ListView):
    """View that shows all from of the current user."""
    model = models.FormData
    ordering = 'title'

    def get_queryset(self):
        return models.FormData.objects.user_related(self.request.user.id)
