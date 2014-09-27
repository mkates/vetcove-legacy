
from django import forms

### The default attrs to add to each input element
TEMPLATE_ATTRS = {
    'class':'form-control',
    'data-invalid':'Required',
    'data-required':'True'
}

###### General Text Input ############
class CoreEmailInput(forms.TextInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'email',
            'data-type':'email',
            'placeholder':'you@example.com',
            'data-invalid':'Invalid Email Address'
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(CoreEmailInput, self).__init__(default_attrs)

###### General Text Input ############
class CoreIntegerInput(forms.NumberInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'number',
            'data-type':'number',
            'data-invalid':'Invalid Number',
            'min':0
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(CoreIntegerInput, self).__init__(default_attrs)

###### General Text Input ############
class CorePhoneNumberInput(forms.TextInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'text',
            'data-type':'phonenumber',
            'placeholder':'(xxx) xxx-xxxx',
            'data-invalid':'Invalid Phone Number',
            'max-length':15
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(CorePhoneNumberInput, self).__init__(default_attrs)

###### Password Input ##################
class CorePasswordInput(forms.PasswordInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'password',
            'data-type':'password',
            'placeholder':'Password',
            'class':'form-control password'
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(CorePasswordInput, self).__init__(default_attrs)

###### Confirm Password Input ##################
class CoreConfirmPasswordInput(forms.PasswordInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'text',
            'data-type':'confirmpassword',
            'placeholder':'Confirm Password',
            'class':'form-control confirmpassword'
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(CoreConfirmPasswordInput, self).__init__(default_attrs)


