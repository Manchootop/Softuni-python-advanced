from django import forms

from exam.cars.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner', ]

        widgets = {
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "https://..."
                },
            ),

        }

class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set fields as readonly
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = True
