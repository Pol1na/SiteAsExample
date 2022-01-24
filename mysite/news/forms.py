from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название недолжно начинаться с цифры')
        return title

    # title = forms.CharField(max_length=50, label='Название статьи',
    #                         widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Текст статьи', widget=forms.Textarea(attrs={'class': 'form-control',
    #                                                                               'rows': 5}))
    # is_published = forms.BooleanField(label='Опубликовать? ', required=False, initial=True,
    #                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Категория',
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
