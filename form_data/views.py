from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import FormDataCreateForm
from .models import FormData


class FormDataCreateView(LoginRequiredMixin, FormView):
    form_class = FormDataCreateForm
    success_url = '/'
    template_name = 'form_data/formdata_create_view.html'

    def form_valid(self, form):
        FormData.objects.create(author=self.request.user, title=form.cleaned_data['title'])
        return redirect(self.get_success_url())
