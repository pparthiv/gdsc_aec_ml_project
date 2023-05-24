from django import forms

class LinearRegressionForm(forms.Form):
    input1 = forms.FloatField(label='Input 1', widget=forms.NumberInput(attrs={'class': 'main-div_1-input input_1'}))
    output1 = forms.FloatField(label='Output 1', widget=forms.NumberInput(attrs={'class': 'main-div_1-input output_1'}))
    input2 = forms.FloatField(label='Input 2', widget=forms.NumberInput(attrs={'class': 'main-div_1-input input_2'}))
    output2 = forms.FloatField(label='Output 2', widget=forms.NumberInput(attrs={'class': 'main-div_1-input output_2'}))
    input3 = forms.FloatField(label='Input 3', widget=forms.NumberInput(attrs={'class': 'main-div_1-input input_3'}))
    output3 = forms.FloatField(label='Output 3', widget=forms.NumberInput(attrs={'class': 'main-div_1-input output_3'}))
    input4 = forms.FloatField(label='Input 4', widget=forms.NumberInput(attrs={'class': 'main-div_1-input input_4'}))
    output4 = forms.FloatField(label='Output 4', widget=forms.NumberInput(attrs={'class': 'main-div_1-input output_4'}))
    input5 = forms.FloatField(label='Input 5', widget=forms.NumberInput(attrs={'class': 'main-div_1-input input_5'}))
    output5 = forms.FloatField(label='Output 5', widget=forms.NumberInput(attrs={'class': 'main-div_1-input output_5'}))
    input_number = forms.FloatField(label='Test Number', widget=forms.NumberInput(attrs={'class': 'main-div_1-input test_number'}))