from braces.views import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView
from rest_framework.authtoken.models import Token

from .forms import FormDataCreateForm
from .models import FormData


class FormDataCreateView(LoginRequiredMixin, FormView):
    form_class = FormDataCreateForm
    success_url = '/'
    template_name = 'form_data/formdata_create_view.html'

    def form_valid(self, form):
        FormData.objects.create(author=self.request.user, title=form.cleaned_data['title'])
        return redirect(self.get_success_url())


class FormDataUpdateView(DetailView):
    template_name = 'form_data/formdata_update_view.html'
    model = FormData

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise PermissionDenied()
        return super(FormDataUpdateView, self).dispatch(request, *args, **kwargs)

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self.request.user)
        return token.key
