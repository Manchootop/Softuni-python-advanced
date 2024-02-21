from django import forms


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=35,
        required=True,
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
    )
