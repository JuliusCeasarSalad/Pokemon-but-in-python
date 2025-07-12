import os, json

ASSET_PATH = f"{os.path.dirname(__file__)}\\Assets"

with open(os.path.join(os.path.dirname(__file__), "Typechart.json")) as fo:
    TYPE_ADVATAGES = json.load(fo)
