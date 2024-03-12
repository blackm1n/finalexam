from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LogoutForm(forms.Form):
    confirm = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label="Я подтверждаю, что выхожу из своего аккаунта.")


class RecipeForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'steps'}))
    cook_time = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cook time in minutes'}))
    image = forms.ImageField(required=False)
