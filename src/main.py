import pandas as pd

def load_data():
    try:
        df = pd.read_csv("data/flights_sample_3m.csv")  # one level up into data folder
        print("✅ Dataset Loaded Successfully!")
        print(f"🔹 Total Rows: {len(df)}")
        print("\n📌 First 5 rows:")
        print(df.head())
    except FileNotFoundError:
        print("❌ Dataset not found. Please make sure the file exists in Milestone1 => data folder.")

if __name__ == "__main__":
    load_data()
