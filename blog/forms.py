from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    check = forms.BooleanField(required=True, label="你同意嗎？")

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            # "category",
            "tags",
        )
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title.startswith("ABC"):
            raise forms.ValidationError("你的文章標題需要以 ABC 開頭")

        return title + " end"

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title", "")
        content = cleaned_data.get("content", "")
        if (len(title) + len(content)) <= 10:
            raise forms.ValidationError("文章太短")

        return cleaned_data
