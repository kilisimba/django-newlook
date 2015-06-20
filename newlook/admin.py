from django.contrib import admin
from django import forms

class NewlookModelAdmin(admin.ModelAdmin):
    change_list_template = 'newlook/change_list.html'
    change_form_template = 'newlook/change_form.html'

    from django.utils.decorators import method_decorator
    from django.views.decorators.csrf import csrf_protect
    @method_decorator(csrf_protect)
    def changelist_view(self, request, extra_context=None):

        # Check actions to see if any are available on this changelist
        actions = self.get_actions(request)

        # Build the action form and populate it with available actions. No default choice.
        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields['action'].choices = self.get_action_choices(request, default_choices=[])
        else:
            action_form = None

        context = dict(
            action_form=action_form,
        )
        context.update(extra_context or {})

        return super(NewlookModelAdmin, self).changelist_view(request, context)

    class Media:
        css = {
            "all":  (
                    "newlook/css/base.css",
                    "newlook/css/changelists.css",
                    )
              }
        js = (	
                '/static/jquery-2.1.1.min.js',
                '/static/jquery-ui-1.11.1.min.js',
                'newlook/js/action_buttons.js',
             )

