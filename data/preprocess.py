import json
import os
import csv
from collections import Counter

# Read JSON file
with open("raw/hatexplain_train.json", "r") as f:
    data_list = [json.loads(line) for line in f]

# Helper functions
def tokens_to_text(tokens):
    return ' '.join(tokens).replace(" .", ".").replace(" ,", ",")

def label_to_severity(label):
    if label == 0:
        return "Low"
    elif label == 1:
        return "Medium"
    elif label == 2:
        return "High"
    else:
        return "Unknown"

# Prepare CSV file
with open("training_data.csv", "w", newline="") as f:
    fieldnames = ["text", "majority_label", "severity", "labels", "annotator_ids", "targets"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for data in data_list:
        # Extract needed fields
        text = tokens_to_text(data["post_tokens"])
        labels = data["annotators"]["label"]
        annotator_ids = data["annotators"]["annotator_id"]
        targets = data["annotators"]["target"]

        # Majority label and severity
        majority = Counter(labels).most_common(1)[0][0]
        severity = label_to_severity(majority)

        # Write row
        writer.writerow({
            "text": text,
            "majority_label": majority,
            "severity": severity,
            "labels": ", ".join(map(str, labels)),
            "annotator_ids": ", ".join(map(str, annotator_ids)),
            "targets": ", ".join({target for group in targets for target in group})
        })
