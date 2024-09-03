import hashlib
import os

# Directory to check
directory = "/path/to/directory"

# File to store hashes
hashfile = "/var/log/file_hashes.txt"

def calculate_hash(filepath):
    hash_algo = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def load_hashes():
    if os.path.exists(hashfile):
        with open(hashfile, "r") as f:
            return dict(line.strip().split() for line in f)
    return {}

def save_hashes(hashes):
    with open(hashfile, "w") as f:
        for filepath, filehash in hashes.items():
            f.write(f"{filehash} {filepath}\n")

def check_integrity():
    previous_hashes = load_hashes()
    current_hashes = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filehash = calculate_hash(filepath)
            current_hashes[filepath] = filehash

            if filepath in previous_hashes and previous_hashes[filepath] != filehash:
                print(f"Warning: File {filepath} has been modified.")

    save_hashes(current_hashes)

check_integrity()
