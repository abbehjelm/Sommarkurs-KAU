from django import forms


class EncryptionForm(forms.Form):
    key = forms.CharField(max_length=44, min_length=3, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'encryptionkey',
        'placeholder': 'Ange din önskade krypteringsnyckel...'
    }))
    iv = forms.CharField(max_length=16, min_length=3, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'initVector',
        'placeholder': 'Ange en startvektor (valfritt men rekommenderas) ...'
    }))
    text = forms.CharField(max_length=1000, min_length=3, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Vad vill du kryptera idag...',
        'rows': '15',
    }))


class DecryptionForm(forms.Form):
    key = forms.CharField(max_length=44, min_length=3, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'encryptionkey',
        'placeholder': 'Ange krypteringsnyckeln...'

    }))
    iv = forms.CharField(max_length=16, min_length=3, required=False,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'initVector',
        'placeholder': 'Ango startvektor (om användes vid kryptering)...'
    }))
    cipher = forms.CharField(max_length=1000, min_length=3, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Vad ska vi dekryptera idag?...',
            'rows': '15',
    }))
