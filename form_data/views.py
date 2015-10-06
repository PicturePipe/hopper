from django import views

from .forms import CreateFormView


class FormDataCreateView(views.FormView):
    form_class = CreateFormView
    success_url = '/'
    template_name = 'form_data/formdata_create_view.html'
