from django.shortcuts import render,render_to_response
from formtools.wizard.views import SessionWizardView

from .forms import InputTypeForm,BodyFormWYSIWYG

FORMS = [("Input_Type",InputTypeForm),
         ("Tutorial_Form",BodyFormWYSIWYG)]

TEMPLATES = {"Input_Type":"tutorials/input_selection.html",
             "Tutorial_Form":"tutorials/create_tutorial.html"}


class CreationWizard(SessionWizardView):
    def get_form_instance( self, step ):
        if(step=="Tutorial_Form"):
            if self.instance is None:
                print get_form_step_data(InputTypeForm)
                self.instance = Tutorial()
            return self.instance

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list,**kwargs):
        self.instance.save()




