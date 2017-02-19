from django import forms

class FileForm(forms.Form):
	docfile = forms.FileField(
		label='Select a file'
	)