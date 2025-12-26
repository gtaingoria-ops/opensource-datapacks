# 🚀 Open Source Startup Name Generator

> A structured, metadata-rich dataset of startup prefixes, buzzwords, and suffixes.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

---

## 💡 The Concept

Most name generators just glue two random words together. This project uses a **Token & Metadata** approach to build names that actually sound like real startups.

We break names down into three components:

| Component | Example | Metadata |
| :--- | :--- | :--- |
| **Prefix** | `Aero` | `{"vibe": "futuristic", "tags": ["hardware"]}` |
| **Root** | `Nexus` | `{"category": "noun", "tags": ["connection"]}` |
| **Suffix** | `ify` | `{"vibe": "trendy", "tags": ["action"]}` |

By filtering these components based on their metadata tags (e.g., "Show me only *medical* roots with a *tech* suffix"), you can generate high-quality names programmatically.

---

## 💻 Requirements

To build the dataset, you only need:

* **Python 3.x** (Tested on 3.8+)
* No external libraries required (No `pip install` needed).

---

## ⚡ How to Use the Data

The database is provided as a single `.json` file (`startup_names.json`). You can use a simple script to combine the tokens.

### Example: The "Silicon Valley" Generator
This Python script loads your database and creates names using the `Root + Suffix` strategy (like *Spotify* or *Shopify*).

```python
import json
import random

# 1. Load the Data
with open('startup_names.json', 'r') as f:
    data = json.load(f)['data']

# 2. Filter for "Trendy" suffixes (e.g., 'ly', 'ify', 'io')
trendy_suffixes = [s for s in data['suffixes'] if 'trendy' in s['vibe']]

# 3. Generate Name
root = random.choice(data['roots'])
suffix = random.choice(trendy_suffixes)

name = root['token'] + suffix['token']
print(f"Your new startup name: {name}")
# Output: "Cloudify" or "Data.io"
