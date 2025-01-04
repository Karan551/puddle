from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from conversation.forms import ConversationMsgForm
from conversation.models import Conversation, ConversationMsg
# Create your views here.


def new_conversation_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if item.created_by == request.user:
        return redirect("dashboard:dashboard_home")

    conversations = Conversation.objects.filter(
        item=item).filter(members__in=[request.user.id])

    if conversations:
        # HERE: we will come again
        pass
    if request.method == "POST":
        form = ConversationMsgForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)

            # conversations.members.add(request.user)
            conversation.members.add(request.user)
            conversation.save()

            conversation_msg = form.save(commit=False)
            conversation_msg.conversation = conversation
            conversation_msg.created_by = request.user
            conversation_msg.save()

            return redirect("item:item_detail", id=item_id)

    form = ConversationMsgForm()
    context = {"form": form}

    return render(request, "conversation/new.html", context)


def inbox(request):
    conversations = Conversation.objects.filter(members=request.user)
    context = {
        "conversations": conversations
    }
    return render(request, "conversation/inbox.html", context)


def conversation_detail_view(request, conversation_id):
    conversation = Conversation.objects.filter(
        members__in=[request.user.id]).get(pk=conversation_id)

    if request.method == "POST":
        form = ConversationMsgForm(request.POST)

        if form.is_valid():
            conversation_msg = form.save(commit=False)
            conversation_msg.created_by = request.user
            conversation_msg.conversation = conversation
            conversation_msg.save()

            conversation.save()

            return redirect("conversation:detail", id=conversation_id)

    form = ConversationMsgForm()
    context = {
        "form": form,
        'conversation': conversation,
    }
    print("this is conversation::", conversation)
    return render(request, "conversation/detail.html", context)
