import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_graphs():
    os.makedirs("output", exist_ok=True)

    df = pd.read_csv("output/processed_emails.csv")

    # Pie Chart - Category Distribution
    plt.figure(figsize=(6, 6))
    df["category"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Category Distribution")
    plt.ylabel("")
    plt.savefig("output/category_distribution.png")
    plt.close()

    # Bar Chart - Top 5 Senders
    plt.figure(figsize=(8, 5))
    df["sender"].value_counts().head(5).plot(kind="bar")
    plt.title("Top 5 Senders")
    plt.xlabel("Sender")
    plt.ylabel("Email Count")
    plt.tight_layout()
    plt.savefig("output/top_senders.png")
    plt.close()

    # Line Chart - Emails Per Day
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    daily = df.groupby(df["date"].dt.date).size()

    plt.figure(figsize=(8, 5))
    daily.plot(marker="o")
    plt.title("Emails Per Day")
    plt.xlabel("Date")
    plt.ylabel("Emails")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/daily_volume.png")
    plt.close()

    print("Analytics graphs created successfully!")