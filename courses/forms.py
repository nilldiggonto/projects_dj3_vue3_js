from django import forms
from .models import ClassDuration,PrefectStudent,CourseInfo
from students.models import Student

CLASS_CHOICES = (
    ('STUDENT','Student'),
    ('TEACHER','Teacher'),
)
class ClassSelectForm(forms.Form):
    class_name = forms.ChoiceField(choices=CLASS_CHOICES,label='',widget=forms.RadioSelect(attrs={}))

class ClassDurationForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(label='select the student', widget= forms.CheckboxSelectMultiple,queryset= Student.objects.filter(is_topper=True))
    class Meta:
        model = ClassDuration
        fields = "__all__"

class CourseInfoForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(label='select the student', widget= forms.CheckboxSelectMultiple,queryset= Student.objects.filter(is_topper=False))

    class Meta:
        model = CourseInfo
        fields = "__all__"