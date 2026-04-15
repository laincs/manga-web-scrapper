import os

def init():
    os.makedirs("results", exist_ok=True)

def clear_file(file):
    open(file, "w").close()

def save_to_txt(file, data):
    with open(file, "w", encoding="utf-8") as f:
        for item in sorted(data):
            f.write(item + "\n")

def load_from_txt(file):
    with open(file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]