from django import forms
from django.template.loader import render_to_string

class MultipleSelectWithPopUp(forms.SelectMultiple):
    def __init__(self, model=None, template='addnew.html'):
        self.model = model
        self.template = template
        super(MultipleSelectWithPopUp, self).__init__()

    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPopUp, self).render(name, *args, **kwargs)

        if not self.model:
            self.model = name

        popupplus = render_to_string(self.template, {'field': name, 'model': self.model})
        return html+popupplus

class SelectWithPopUp(forms.Select):
    def __init__(self, model=None, template='addnew.html'):
        self.model = model
        self.template = template
        super(SelectWithPopUp, self).__init__()

    def render(self, name, *args, **kwargs):
        html = super(SelectWithPopUp, self).render(name, *args, **kwargs)

        if not self.model:
            self.model = name

        popupplus = render_to_string(self.template, {'field': name, 'model': self.model})
        return html+popupplus
