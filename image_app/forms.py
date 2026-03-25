from django import forms

OPERATIONS = [
    ('inversion', 'Inversion'),
    ('decalage', 'Décalage additif'),
    ('mise_echelle', 'Mise à l’échelle'),
    ('rotation', 'Rotation'),
    ('miroir', 'Miroir'),
    ('kmeans', 'K-means'),
    ('seuillage', 'Seuillage'),
    ('region_growing', 'Region Growing'),
]

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Choisir une image')
    operation = forms.ChoiceField(choices=OPERATIONS, label='Opération')
    param = forms.IntegerField(label='Paramètre (optionnel)', required=False)