from django.forms import ModelForm
from item.models import Item
from django import forms


CSS_CLASSES = "w-full px-6 py-4 border rounded-xl mb-2  text-lg md:text-xl outline-none focus:ring-1 focus:ring-indigo-600"


class AddItemForm(ModelForm):
    class Meta:
        model = Item

        fields = ["category", "name", "description", "image", "price"]

        labels = {
            "category": "Category :",
            "name": "Product Name:",
            "description": "Product Description:",
            "image": "Product Image:",
            "price": "Product Price:",
        }

        widgets = {
            "category": forms.Select(attrs={"class": CSS_CLASSES}),

            "name": forms.TextInput(attrs={
                "class": CSS_CLASSES,
                "placeholder": "Enter Product Name Here...."
            }),
            "description": forms.Textarea(attrs={
                "class": CSS_CLASSES,
                "rows": 8,
                "cols": 10,
                "placeholder": "Enter Product Description Here...."
            }),
            "image": forms.FileInput(attrs={
                "class": CSS_CLASSES
            }),
            "price": forms.TextInput(attrs={
                "class": CSS_CLASSES,
                "placeholder": "Enter Product Price Here...."
            })
        }


class EditItemForm(AddItemForm):
    class Meta(AddItemForm.Meta):

        fields = AddItemForm.Meta.fields + ["is_sold"]
