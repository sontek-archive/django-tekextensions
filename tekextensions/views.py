from django.forms.models import modelform_factory
from django.db.models.loading import get_models, get_app, get_apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape

@login_required
def add_new_model(request, model_name):
    if (model_name.lower() == model_name):
        normal_model_name = model_name.capitalize()
    else:
        normal_model_name = model_name
    app_list = get_apps()
    for app in app_list:
        for model in get_models(app):
            if model.__name__ == normal_model_name: 
                form = modelform_factory(model)

                if request.method == 'POST':
                    form = form(request.POST)
                    if form.is_valid():
                        try:
                            new_obj = form.save()
                        except forms.ValidationError, error:
                            new_obj = None

                        if new_obj:
                            return HttpResponse('<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' % \
                                (escape(new_obj._get_pk_val()), escape(new_obj)))

                else:
                    form = form()

                page_context = {'form': form, 'field': normal_model_name}
                return render_to_response('popup.html', page_context, context_instance=RequestContext(request))
    raise Exception('Did not find the model %s' % (normal_model_name))
