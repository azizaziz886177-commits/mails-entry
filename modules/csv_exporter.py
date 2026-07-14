import pandas as pd
import os

def export_processed_emails(data):
    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv("output/processed_emails.csv", index=False)

    print("processed_emails.csv created successfully")


def export_entities(data):
    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv("output/extracted_entities.csv", index=False)

    print("extracted_entities.csv created successfully")