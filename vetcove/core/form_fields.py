
from django import forms

### The default attrs to add to each input element
TEMPLATE_ATTRS = {
    'class':'form-control',
    'data-invalid':'Required',
    'data-required':True
}

###### General Text Input ############
class TextInput(forms.TextInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'text',
            'data-type':'text',
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(TextInput, self).__init__(default_attrs)

###### Email Input ###################
class EmailInput(forms.TextInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'email',
            'data-type':'email',
            'placeholder':'Email Address'
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(EmailInput, self).__init__(custom_attrs)

###### Password Input ##################
class PasswordInput(forms.PasswordInput):
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
        super(PasswordInput, self).__init__(default_attrs)

###### Confirm Password Input ##################
class ConfirmPasswordInput(forms.PasswordInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'text',
            'data-type':'text',
            'placeholder':'Confirm Password',
            'class':'form-control confirmpassword'
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(ConfirmPasswordInput, self).__init__(default_attrs)

###### Select Input ##################
class Select(forms.Select):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'select',
            'data-type':'select'
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(Select, self).__init__(default_attrs)

###### Select Input ##################
class CheckboxInput(forms.CheckboxInput):
     def __init__(self, attrs=None):
        default_attrs = dict(TEMPLATE_ATTRS)
        custom_attrs = {
            'type':'checkbox',
            'data-type':'checkbox',
            'class':''
        }
        default_attrs.update(custom_attrs)
        if attrs:
            default_attrs.update(attrs)
        super(CheckboxInput, self).__init__(default_attrs)



