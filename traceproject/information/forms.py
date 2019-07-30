from django.forms import ModelForm
from .models import Jikbang

class Jikbang2(ModelForm):
    class Meta:
        model = Jikbang
        fields = [ 'image', 'title','body' ]