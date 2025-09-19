import hashlib
import os
import config

def get_dml_hash():
    try:
        with open(config.DML_SOURCE_FILE, 'rb') as f:
            file_bytes = f.read()
            hasher = hashlib.sha256()
            hasher.update(file_bytes)
            return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Could not find file {config.DML_SOURCE_FILE}")
        return None