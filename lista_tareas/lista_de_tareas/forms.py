from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título de la tarea...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añade clases CSS a los campos del formulario
        self.fields['titulo'].widget.attrs.update({'class': 'form-input'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-select'})