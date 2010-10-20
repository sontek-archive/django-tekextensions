settings.py
====================
    TEMPLATE_CONTEXT_PROCESSORS = (
        'tekextensions.context_processors.admin_media_prefix',
    )
    INSTALLED_APPS = (
        'tekextensions',
    )

urls.py
====================
    url(r'^add/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_model'),

forms.py
====================
>override any ModelChoiceField widget with SelectWithPopUp

    from tekextensions.widgets import SelectWithPopUp
    from django import forms
    
    class CustomForm(forms.Form):
        company = forms.ModelChoiceField(CustomModel.objects, widget=SelectWithPopUp)
