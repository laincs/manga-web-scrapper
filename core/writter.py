import os

def init():
    os.makedirs("results", exist_ok=True)

def clear_file(file):
    open(file, "w").close()

def save_to_txt(file, data):
    with open(file, "w", encoding="utf-8") as f:
        for item in sorted(data):
            f.write(item + "\n")