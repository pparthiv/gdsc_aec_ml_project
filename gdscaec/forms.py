from django import forms

class LinearRegressionForm(forms.Form):
    input1 = forms.FloatField(label='Input 1')
    input2 = forms.FloatField(label='Input 2')
    input3 = forms.FloatField(label='Input 3')
    input4 = forms.FloatField(label='Input 4')
    input5 = forms.FloatField(label='Input 5')
    output1 = forms.FloatField(label='Output 1')
    output2 = forms.FloatField(label='Output 2')
    output3 = forms.FloatField(label='Output 3')
    output4 = forms.FloatField(label='Output 4')
    output5 = forms.FloatField(label='Output 5')
    input_number = forms.FloatField(label='Test Number')