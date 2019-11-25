from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('question', 'created_date', 'author', 'text')

    def __init__(self, question_pk=None, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
     