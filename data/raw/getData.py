from datasets import load_dataset
import json

splits = ["train", "test", "validation"]

# Step 1: Download and save JSON files
for split in splits:
    dataset = load_dataset("hatexplain", split=split)
    dataset.to_json(f"hatexplain_{split}.json")

# Step 2: Reload from JSON files
data_files = {split: f"hatexplain_{split}.json" for split in splits}
hatexplain_ds = load_dataset("json", data_files=data_files)

# Open and read the JSON file
with open('hatexplain_train.json', 'r') as file:
    lines = file.readlines()
    hs_df = [json.loads(line) for line in lines]

print(hs_df[0])  # first datapoint

