from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário',
            }
        ),
    )

    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
    )

class CadastroForm(forms.Form):
    username = forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário',
            }
        ),
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }
        ),
    )

    password1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
    )

    password2 = forms.CharField(
        label='Confirme a senha',
        required=True,
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme a senha',
            }
        ),
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username:
            username = username.lower().strip()

            if ' ' in username:
                raise forms.ValidationError('O nome de usuário não pode conter espaços!')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            email = email.lower().strip()

            if not '@' in email or not '.' in email:
                raise forms.ValidationError('E-mail inválido!')

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            if len(password1) < 8:
                raise forms.ValidationError('A senha deve conter no mínimo 8 caracteres!')
            if password1.isdigit():
                raise forms.ValidationError('A senha deve conter letras!')
            if password1.isalpha():
                raise forms.ValidationError('A senha deve conter números!')
            if password1.islower():
                raise forms.ValidationError('A senha deve conter letras maiúsculas!')
            if password1.isupper():
                raise forms.ValidationError('A senha deve conter letras minúsculas!')
            if password1.isalnum():
                raise forms.ValidationError('A senha deve conter caracteres especiais!')

        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('As senhas não coincidem!')

        return password2