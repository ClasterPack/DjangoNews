from django import forms

from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=250)
    slug = forms.SlugField(max_length=250)
    content = forms.CharField()
    status = forms.ChoiceField()


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'status']

    def clean(self):
        data = self.clean_data
        title = data.get("title")
        qs = Post.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("Оглавление", f"\"{title}\" уже используеться/")
        return data
