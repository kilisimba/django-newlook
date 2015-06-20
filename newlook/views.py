from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.admin import site

class MainView(TemplateView):
    template_name = 'admin/base_site.html'

    # Every instance of ProtectedView will now have login protection.
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MainView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MainView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['site_title'] = 'DPA'
        context['site_header'] = 'DPA Your Django Personal Accountant'
        site_context = site.each_context()
        context['main_menu'] = site_context['main_menu']
        #context['main_menu'] = { 
        #                        'DPA': reverse('main'), 
        #                        'Commodity': reverse('admin:index'), 
        #                        'Amin': reverse('admin:index'), 
        #                      }
        return context
