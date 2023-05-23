from django import forms

class LinearRegressionForm(forms.Form):
    input1 = forms.FloatField(label='Input 1', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    output1 = forms.FloatField(label='Output 1', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    input2 = forms.FloatField(label='Input 2', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    output2 = forms.FloatField(label='Output 2', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    input3 = forms.FloatField(label='Input 3', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    output3 = forms.FloatField(label='Output 3', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    input4 = forms.FloatField(label='Input 4', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    output4 = forms.FloatField(label='Output 4', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    input5 = forms.FloatField(label='Input 5', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    output5 = forms.FloatField(label='Output 5', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))
    input_number = forms.FloatField(label='Test Number', widget=forms.NumberInput(attrs={'style':'width: 300px', 'class': 'linreg_label'}))