
from django import forms
from localflavor.us.us_states import US_STATES


class CoreTextInput(forms.TextInput):
     '''
     Standard Text Input
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'text',
            'data-type':'text',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CoreTextInput, self).__init__(default_attrs)


class CoreCheckboxInput(forms.CheckboxInput):
     '''
     Checkbox Input
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'checkbox',
            'data-type':'checkbox',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CoreCheckboxInput, self).__init__(default_attrs)


class CoreSelect(forms.Select):
     '''
     Standard Select Input
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'data-type':'select',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CoreSelect, self).__init__(default_attrs)


class CorePostalCodeInput(forms.TextInput):
     '''
     Postal Code Input
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'text',
            'data-type':'postalcode',
            'maxlength':5,
            'placeholder':'xxxxx'
        }
        if attrs:
            default_attrs.update(attrs)
        super(CorePostalCodeInput, self).__init__(default_attrs)


class CoreEmailInput(forms.TextInput):
     '''
     Email Input
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'email',
            'data-type':'email',
            'placeholder':'you@example.com',
            'data-errormessage':'This is an invalid email address'
        }
        if attrs:
            default_attrs.update(attrs)
        super(CoreEmailInput, self).__init__(default_attrs)


class CorePositiveIntegerInput(forms.NumberInput):
     '''
     Sets a minimum value so only positive integers are allowed
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'number',
            'data-type':'number',
            'placeholder': '0+',
            'data-errormessage':'Invalid Number',
            'min':0
        }
        if attrs:
            default_attrs.update(attrs)
        super(CorePositiveIntegerInput, self).__init__(default_attrs)


class CorePhoneNumberInput(forms.TextInput):
     '''
     Phone Numbers
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'text',
            'data-type':'phonenumber',
            'placeholder':'(xxx) xxx-xxxx',
            'data-errormessage':'Phone number must be in format (xxx) xxx-xxxx',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CorePhoneNumberInput, self).__init__(default_attrs)


class CorePasswordInput(forms.PasswordInput):
     '''
     Passwords
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'password',
            'data-type':'password',
            'placeholder':'Password',
            'data-errormessage':'Passwords must be at least 8 characters',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CorePasswordInput, self).__init__(default_attrs)


class CoreConfirmPasswordInput(forms.PasswordInput):
     '''
     Confirm Password Field
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'password',
            'data-type':'confirmpassword',
            'placeholder':'Confirm Password',
            'data-errormessage':'Passwords do not match',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CoreConfirmPasswordInput, self).__init__(default_attrs)


class CoreFileInput(forms.FileInput):
     '''
     Core File Input
     '''
     def __init__(self, attrs=None):
        default_attrs = {
            'type':'file',
            'data-type':'file',
        }
        if attrs:
            default_attrs.update(attrs)
        super(CoreFileInput, self).__init__(default_attrs)


class CoreStateSelect(CoreSelect):
    '''
    Select field with states
    '''
    def __init__(self, attrs=None, choices=()):
        super(CoreStateSelect, self).__init__(attrs)
        state_choices = [('','------')]+[state for state in US_STATES]
        self.choices = list(state_choices)


class CoreMonthSelect(CoreSelect):
    '''
    Select field for months
    '''
    def __init__(self, attrs=None, choices=()):
        super(CoreMonthSelect, self).__init__(attrs)
        month_choices = (('','-----'),(1,'January'),(2,'February'),(3,'March'),(4,'April'),(5,'May'),(6,"June"),(7,"July"),
            (8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December'))
        self.choices = list(month_choices)

class CoreDaySelect(CoreSelect):
    '''
    Select field for months
    '''
    def __init__(self, attrs=None, choices=()):
        super(CoreDaySelect, self).__init__(attrs)
        day_choices = [('','-----')]+[(day,day) for day in range(0,31)]
        self.choices = list(day_choices)

class CoreFutureYearSelect(CoreSelect):
    '''
    Select field for months
    '''
    def __init__(self, attrs=None, choices=()):
        super(CoreFutureYearSelect, self).__init__(attrs)
        year_choices = [('','-----')]+[(year,year) for year in range(2014,2024)]
        self.choices = list(year_choices)

