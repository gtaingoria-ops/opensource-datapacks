# 🛠️ How to Generate the Database

This guide explains the step-by-step process to generate the `startup_names.json` file using the build script.

---

## 1. Input (Edit the Data)

Open `build_dataset.py` in your code editor. At the top of the file, you will find the **Raw Data Lists**. Add your new words here.

```python
# --- RAW DATA LISTS ---

# 1. Add Prefixes (short starting words)
prefixes_raw = [
    "aero", "alfa", "algo", "YOUR_NEW_PREFIX_HERE"
]

# 2. Add Roots (main nouns/verbs)
roots_raw = [
    "code", "cloud", "star", "YOUR_NEW_ROOT_HERE"
]

# 3. Add Suffixes (endings)
suffixes_raw = [
    "ify", "ly", "io", "YOUR_NEW_SUFFIX_HERE"
]
```

> **Note:** Ensure every word is wrapped in quotes `""` and separated by a comma `,`.

---

## 2. Process (Run the Script)

Once your words are added, you must run the script to process the data and assign metadata. Open your terminal in the project directory and run:

```bash
python build_dataset.py
```

> **What happens:** The script reads the raw lists, runs them through the `get_tags()` and `get_vibe()` functions to assign metadata automatically, and compiles the JSON structure.

---

## 3. Output (Verify the File)

If the script runs successfully, it will overwrite `startup_names.json` with the new data. You will see a success message:

```text
> Successfully generated 'startup_names.json' with 2150 tokens.
```

> **Verification:** Open `startup_names.json` to confirm your new words have been added and tagged correctly.

---

## 4. Advanced (Custom Logic)

If you want to change how the script assigns tags (e.g., to automatically tag "crypto" words), you can edit the helper functions inside `build_dataset.py`.

Locate the `get_tags` function:

```python
def get_tags(word):
    tags = []
    
    # Existing logic
    if len(word) < 4: tags.append("short")
    
    # ADD YOUR NEW LOGIC:
    if word in ["coin", "chain", "ledger"]:
        tags.append("crypto")
        
    return tags
```

After modifying the logic, **repeat Step 2** to regenerate the database with the new rules.
