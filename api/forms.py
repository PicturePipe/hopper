# encoding: utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, ButtonHolder, Field, Fieldset, Layout, Submit
from crispy_forms.utils import render_crispy_form
from django import forms
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


class HopperForm(forms.Form):

    type_field_mapping = {
        'input': forms.CharField,
        'textarea': forms.CharField,
        'radio': forms.ChoiceField,
        'checkbox': forms.BooleanField,
        'select': forms.ChoiceField,
        'multiselect': forms.MultipleChoiceField,
        'date': forms.DateField,
        'datetime': forms.DateTimeField,
        'file': forms.FileField,
        'integer': forms.IntegerField,
        'mail': forms.EmailField,
        'url': forms.URLField,
        'password': forms.CharField,
        'hidden': forms.CharField,
    }

    type_widget_mapping = {
        'textarea': forms.widgets.Textarea,
        'radio': forms.widgets.RadioSelect,
        'password': forms.widgets.PasswordInput,
        'hidden': forms.widgets.HiddenInput,
    }

    def __init__(self, *args, **kwargs):
        model_data = self.get_dict(kwargs.pop('data', None))
        super(HopperForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = model_data['form']['css_classes']
        self.helper.form_action = model_data['form']['action']
        self.helper.form_method = model_data['form']['method']
        self.helper.field_class = model_data['form']['elements_css_classes']
        self.fields, field_layout = self.create_fields(model_data['form']['elements'])
        self.helper.layout = Layout(*field_layout)

    def create_fields(self, elements):
        """Creates dictionary with fields and its attributes and
        widgets"""
        fields = {}
        field_layout = []
        for name, element in elements.items():
            field_attrs = self.get_field_attrs(element)
            if element['type'] == 'fieldset':
                subfields, subfield_layout = self.create_fields(element['elements'])
                fields.update(subfields)
                field_layout.append(Fieldset(element['label'], *subfield_layout))
            else:
                widget = self.create_widget(element)
                if widget:
                    field_attrs['widget'] = widget
                fields[name] = self.type_field_mapping[element['type']](**field_attrs)
                if element['type'] == 'radio':
                    field_layout.append(
                        HTML(fields[name].widget.render(name, ''))  # ToDo: add default
                    )
                else:
                    field_layout.append(Field(name))
        return fields, field_layout

    def create_widget(self, element):
        """Creates widget by type with its attributes"""
        widget = None
        data = element.copy()
        widget_type = data.pop('type', None)
        if widget_type in self.type_widget_mapping:
            widget_attrs = self.get_widget_attrs(data, widget_type)
            widget = self.type_widget_mapping[widget_type](attrs=widget_attrs)
        return widget

    def get_base_field_attrs(self, data):
        """Returns dictionary with general field attributes"""
        field_attrs = self.build_dict(data, ['required'])
        field_attrs['initial'] = data.get('default')
        return field_attrs

    def get_base_widget_attrs(self, data):
        """Returns dictionary with general widget attributes"""
        return self.build_dict(data, ['immutable', 'readonly'])

    def get_field_attrs(self, data):
        field_attrs = {}
        field_type = data['type']
        if field_type in ['input', 'textarea']:
            field_attrs['max_length'] = data.get('maxlength')
        elif field_type in ['select', 'multiselect', 'radio']:
            field_attrs['choices'] = tuple([(choice, choice) for choice in data['choices']])
        field_attrs.update(self.get_base_field_attrs(data))
        return field_attrs

    def get_widget_attrs(self, data, widget_type):
        """Returns dictionary with attributes for given widget_type"""
        widget_attrs = {}
        if widget_type == 'input':
            widget_attrs = self.build_dict(data, ['label', 'maxlength', 'default'])
        elif widget_type == 'textarea':
            widget_attrs = self.build_dict(data, ['rows', 'cols', 'label'])
        elif widget_type == 'checkbox':
            widget_attrs = self.build_dict(data, ['checked', 'value'])
        widget_attrs.update(self.get_base_widget_attrs(data))
        return widget_attrs

    @classmethod
    def build_dict(cls, source, keys):
        """Builts a dictionary from given keys and source"""
        return {attr: source.get(attr, False) for attr in keys}

    def render_as_form(self):
        """Wrapper function to call crispyforms function"""
        return render_crispy_form(self).strip('\n')

    def get_dict(self, data):
        if type(data) != dict:
            stream = BytesIO(data)
            data = JSONParser().parse(stream)
        return data
