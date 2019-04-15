from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_at' , 'updated_at')

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            return forms.ValidationError('The price must be greater than zero')
        return self.cleaned_data['price']

class ProductAddFormToCart(forms.Form):
    quantity = forms.IntegerField(
        widget = forms.TextInput(
            attrs={'size':'2' , 'class':'quantity' , 'maxlength':'5'},
            error_messages = {'invalid':'please enter a valid number'},
            min_value = 1
        )
    )

    slug = forms.CharField(
        widget = forms.HiddenInput()
    )

    #so this is to override form's constructor
    def __init__(self , request = None , *args, **kwargs):
        super(ProductAddFormToCart , self).__init__(*args , **kwargs)

    #check for cookies
    def cookie_check(self):
        if self.request:
            if not self.request.session.test_cookie_word():
                raise forms.ValidationError('Please enable cookies to add items to your browser')
        return self.cleaned_data