import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

# --- Core Project Paths ---
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# --- File and Directory Paths ---
DB_DIR = resource_path('data')
DB_FILE = os.path.join(DB_DIR, 'PokeData.fs')
DML_VERSION_FILE = resource_path('dml_version.txt')
DML_SOURCE_FILE = resource_path('pokemon_dml.py') # For version_control.py
PICKLE_MODEL_FILE = resource_path('pickle_model')
ASSETS_DIR = resource_path('assets')

# --- Asset Paths Dictionary ---
ASSET_PATHS = {
    "types": os.path.join(ASSETS_DIR, "icons", "{}.gif"),
    "categories": os.path.join(ASSETS_DIR, "icons", "{}.png"),
    "stats": os.path.join(ASSETS_DIR, "icons", "{}.gif"),
    "pokeballs": os.path.join(ASSETS_DIR, "pokeballs", "{}"),
    "sprites": os.path.join(ASSETS_DIR, "PokemonSprites", "{}"),
    "shiny_star": os.path.join(ASSETS_DIR, "icons", "ShinyVIStar.png"),
    "item_icon": os.path.join(ASSETS_DIR, "icons", "item.png"),
    "male_icon": os.path.join(ASSETS_DIR, "icons", "male.png"),
    "female_icon": os.path.join(ASSETS_DIR, "icons", "female.png")
}