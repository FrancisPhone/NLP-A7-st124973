from django.shortcuts import render
from .utils import classify_text
from .models import History


def home(request):
    result = None
    history = History.objects.all().order_by("-created_at")  # Retrieve all history entries

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        model_type = request.POST.get("model_type")  # Get the selected model type
        result = classify_text(user_input, model_type)

        # Add the classification result to the history
        History.objects.create(text=user_input, result=result, model_type=model_type)

    return render(request, "home.html", {"result": result, "history": history})