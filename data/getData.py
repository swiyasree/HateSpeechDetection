from datasets import load_dataset
import json
import os

splits = ["train", "test", "validation"]
raw_dir = "data/raw"  # relative path from your Python file

# Step 1: Download and save JSON files
for split in splits:
    dataset = load_dataset("hatexplain", split=split)
    dataset.to_json(os.path.join(raw_dir, f"hatexplain_{split}.json"))

# Step 2: Reload from JSON files
data_files = {split: os.path.join(raw_dir, f"hatexplain_{split}.json") for split in splits}
hatexplain_ds = load_dataset("json", data_files=data_files)

# Open and read the train JSON file
with open(os.path.join(raw_dir, 'hatexplain_train.json'), 'r') as file:
    lines = file.readlines()
    hs_df = [json.loads(line) for line in lines]

print(hs_df[0])
