#!/usr/bin/env python3

import json
import random
from datetime import datetime, timedelta

sample_texts = [
    "Ran went pretty well but was tired.",
    "Ran early in the morning on the lakefront.",
    "Ran late at night and felt really tired.",
    "Ran in the middle of the day and it was really hot.",
    "Ran in the middle of the day and it was really cold.",
    "Had a problem with my ankle and stopped running.",
]


if __name__ == "__main__":
    start_date = datetime(2020, 1, 1)

    entries = []
    for i in range(1, 366):
        current_date = start_date + timedelta(days=i - 1)
        entries.append({
            "title": f"run {i}",
            "date": current_date.strftime("%Y-%m-%d"),
            "url": "https://google.com",
            "text": random.choice(sample_texts)
        })

    data = {"Sample List": entries}

    with open("sample_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Generated sample_data.json with 365 entries successfully.")