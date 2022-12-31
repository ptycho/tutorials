#!/bin/env python3
import json
import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--actions", action="store_true", help="GitHub actions")
args = parser.parse_args()

# Source notebooks
if args.actions:
    notebook_dir = os.path.dirname(__file__) + "/../notebooks/"
else:
    notebook_dir = os.path.dirname(__file__) + "/../converted/"
notebooks = glob.glob(notebook_dir + "*/*.ipynb")

def replace_div_with_admonition(cell, label="Note", type="note"):
    text = cell["source"][1:-1]
    text[0] = text[0].split("<br>")[1]
    for i,t in enumerate(text):
        if "<pre><code>" in t:
            text[i] = t.replace("<pre><code>", "```python\n")
        if "</code></pre>" in t:
            text[i] = t.replace("</code></pre>", "```")
    new = ['`````{admonition} ' + label + ' \n', ':class: ' + type + '\n', '`````']
    new[2:2] = text
    cell["source"] = new

for name in notebooks:    
    nb = json.load(open(name))
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown":
            for s in cell["source"]:
                if s.startswith("<div class=") and ("warning" in s):
                    replace_div_with_admonition(cell, label="Exercise", type="attention")
                if s.startswith("<div class=") and ("success" in s):
                    replace_div_with_admonition(cell, label="Tip", type="tip")
                if s.startswith("<div class=") and ("info" in s):
                    replace_div_with_admonition(cell, label="Note", type="note")
                if s.startswith("<div class=") and ("danger" in s):
                    replace_div_with_admonition(cell, label="Todo", type="danger")
    json.dump(nb, open(name,"w"))



            


