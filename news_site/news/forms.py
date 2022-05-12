from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=250)
    slug = forms.SlugField(max_length=250)
    content = forms.CharField()
    status = forms.ChoiceField()
