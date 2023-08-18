from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField( max_length=50, required=True)
    DNI = forms.IntegerField(required=True)
    email = forms.EmailField(label="Email", required=False)
    TURNOS = (
        (1,"Mañana"),
        (2,"Tarde"),
        (3,"Noche"),
    )
    turno = forms.ChoiceField(label="Turno elegido", choices=TURNOS, required=True)
    descuento = forms.BooleanField()