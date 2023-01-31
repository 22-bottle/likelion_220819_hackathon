from django import forms
from .models import Course, Lecture

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs = {
            'class':'form-control',
            'placeholder':"title",
            'rows':20,
            'size':100
        }

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['lecture', 'url']
    
    def __init__(self, *args, **kwargs):
        super(LectureForm, self).__init__(*args, **kwargs)

        self.fields['lecture'].widget.attrs = {
            'class':'form-control',
            'placeholder':"lecture",
            'rows':20,
            'cols':100,
        }

        self.fields['url'].widget.attrs = {
            'class':'form-control',
            'placeholder':"url",
            'rows':20,
            'cols':100,
        }