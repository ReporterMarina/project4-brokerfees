# from transformers import AutoModelForSequenceClassification, AutoTokenizer

# model = AutoModelForSequenceClassification.from_pretrained("ReporterMarina/autotrain-clean-broker-fee-81843141864", use_auth_token=True)

# tokenizer = AutoTokenizer.from_pretrained("ReporterMarina/autotrain-clean-broker-fee-81843141864", use_auth_token=True)

# inputs = tokenizer("I love AutoTrain", return_tensors="pt")

# outputs = model(**inputs)

# mykey- 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

#$curl -X POST -H "Authorization: Bearer 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" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/ReporterMarina/autotrain-more_brokers-81853141865


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("ReporterMarina/autotrain-binary_brokers-81863141870")
model = AutoModelForSequenceClassification.from_pretrained("ReporterMarina/autotrain-binary_brokers-81863141870")

# tokenizer = AutoTokenizer.from_pretrained("ReporterMarina/autotrain-more_brokers-81853141865")
# model = AutoModelForSequenceClassification.from_pretrained("ReporterMarina/autotrain-more_brokers-81853141865")

# List of apartment listings
apartment_listings = [
    "Spacious 2-bedroom apartment with great amenities.",
    "No broker fee! Cozy studio apartment in downtown.",
    "Beautiful 3-bedroom apartment with stunning views.",
    "Contact us for more details about this listing.",
    "The building has a lobby, mini- gym, roof deck w/ grill and patio furniture! First month's rent, full month security deposit and broker's fee required."
]

# Tokenize the text inputs
inputs = tokenizer(apartment_listings, return_tensors="pt", padding=True, truncation=True)

# Make predictions
with torch.no_grad():
    logits = model(**inputs).logits

# Convert logits to probabilities using softmax
probs = torch.softmax(logits, dim=1)

# Interpret predictions
label_map = {0: "Broker Fee", 1: "No Broker Fee", 2: "Unknown"}
predictions = [label_map[prediction.item()] for prediction in probs.argmax(dim=1)]

# Print predictions for each apartment listing
for listing, prediction in zip(apartment_listings, predictions):
    print(f"Apartment: {listing}")
    print(f"Prediction: {prediction}")
    print()
