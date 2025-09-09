import hashlib

DML_FILE_PATH = 'pokemon_dml.py'

def get_dml_hash():
    try:
        with open(DML_FILE_PATH, 'rb') as f:
            file_bytes = f.read()
            hasher = hashlib.sha256()
            hasher.update(file_bytes)
            return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Could not find file {DML_FILE_PATH}")
        return None