from conversation.models import ConversationMsg
from django import forms


class ConversationMsgForm(forms.ModelForm):
    class Meta:
        model = ConversationMsg
        fields = ["content"]

        labels = {
            "content": "Message :"
        }
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "w-full px-6 py-4  border rounded-xl text-lg outline-none focus:ring-1 focus:ring-indigo-600",
                "placeholder": "Enter Your Message Here.."
            })
        }
