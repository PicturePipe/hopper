# encoding: utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.utils import render_crispy_form
from django import forms
from django.forms.widgets import (CheckboxSelectMultiple, DateInput, DateTimeInput, EmailInput,
                                  FileInput, HiddenInput, MultiWidget, NumberInput, PasswordInput,
                                  RadioSelect, Select, SelectMultiple, Textarea, TextInput,
                                  URLInput)


class HopperForm(forms.Form):
    def __init__(self, *args, **kwargs):
        model = kwargs.pop('model', None)
        elements = model.convert_to_dict(model.elements)
        super(HopperForm, self).__init__(*args, **kwargs)
        self.type_widget_mapping = {
            'input': TextInput,
            'fieldset': MultiWidget,
            'textarea': Textarea,
            'radio': RadioSelect,
            'checkbox': CheckboxSelectMultiple,
            'select': Select,
            'multiselect': SelectMultiple,
            'date': DateInput,
            'datetime': DateTimeInput,
            'file': FileInput,
            'integer': NumberInput,
            'mail': EmailInput,
            'url': URLInput,
            'password': PasswordInput,
            'hidden': HiddenInput,
        }
        self.helper = FormHelper()
        self.helper.form_class = model.css_classes
        self.helper.form_action = model.action
        self.helper.form_method = model.method
        self.helper.field_class = model.elements_css_classes
        self.fields = self.create_fields(elements)

    def create_fields(self, elements):
        """Creates dictionary with fields and its attributes and
        widgets"""
        fields = {}
        for name, element in elements.items():
            field_attrs = self.get_base_field_attrs(element)
            fields[name] = forms.Field(field_attrs, widget=self.create_widget(element))
            if element['type'] == 'fieldset':
                fields.update(self.create_fields(element['elements']))
        return fields

    def create_widget(self, element):
        """Creates widget by type with its attributes"""
        widget = None
        data = element.copy()
        try:
            widget_type = data.pop('type', None)
            widget_attrs = self.get_widget_attrs(data, widget_type)
            widget = self.type_widget_mapping[widget_type](attrs=widget_attrs)
        except KeyError:
            # no corresponding widget for given type
            raise
        return widget

    def get_base_field_attrs(self, data):
        """Returns dictionary with general field attributes"""
        return self.build_dict(data, ['required'])

    def get_base_widget_attrs(self, data):
        """Returns dictionary with general widget attributes"""
        return self.build_dict(data, ['immutable', 'readonly'])

    def get_widget_attrs(self, data, widget_type):
        """Returns dictionary with attributes for given widget_type"""
        widget_attrs = {}
        if widget_type == 'input':
            widget_attrs = self.build_dict(data, ['label', 'maxlength', 'default'])
        elif widget_type == 'textarea':
            widget_attrs = self.build_dict(data, ['rows', 'cols', 'label'])
        elif widget_type == 'checkbox':
            widget_attrs = self.build_dict(data, ['checked', 'value'])
        else:
            pass
        widget_attrs.update(self.get_base_widget_attrs(data))
        return widget_attrs

    @classmethod
    def build_dict(cls, source, keys):
        """Builts a dictionary from given keys and source"""
        return {attr: source[attr] for attr in keys}

    def render_as_form(self):
        """Wrapper function to call crispyforms function"""
        return render_crispy_form(self).strip('\n')
