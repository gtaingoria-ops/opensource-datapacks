# Contributing to the Startup Name Generator

We love pull requests! If you have cool new startup words, here is how to add them.

## Rules for Adding Words

1.  **Keep it "Startup-y":** We want words like *Zen*, *Flux*, and *Nexus*. We do not want generic words like *Table* or *Shoe*.
2.  **Check Spelling:** Ensure your words are spelled correctly.
3.  **No Duplicates:** The build script does not currently auto-deduplicate, so please check if the word exists first.

## Process

1.  Open `build_dataset.py`.
2.  Add your word to the appropriate list (`prefixes_raw`, `roots_raw`, or `suffixes_raw`).
3.  Run `python build_dataset.py` to ensure it builds without error.
4.  Commit your changes and push a PR!
