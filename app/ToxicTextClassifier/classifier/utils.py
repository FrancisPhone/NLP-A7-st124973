import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the pre-trained models and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
base_model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2  # Ensure this matches the number of labels in your task
)


# Load the even, odd, and LoRA models
even_model = AutoModelForSequenceClassification.from_pretrained("../../student_model_even")
odd_model = AutoModelForSequenceClassification.from_pretrained("../../student_model_odd")
lora_model = PeftModel.from_pretrained(base_model, "../../model_lora")


def classify_text(text, model_type):
    # Select the model based on the user's choice
    if model_type == "even":
        model = even_model
    elif model_type == "odd":
        model = odd_model
    elif model_type == "lora":
        model = lora_model
    else:
        raise ValueError("Invalid model type")

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted label
    predicted_label = outputs.logits.argmax(dim=-1)

    # Return the result
    return "Toxic" if predicted_label == 0 else "Non-Toxic"