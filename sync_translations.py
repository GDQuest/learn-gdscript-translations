"""Merges updates from the template files into the translation files."""
import os
import subprocess

import sys

HELP_TEXT = """Merges updates from the translation template files (.pot files) into the translation files (.po).

The script operates automatically in this repository.

Before running it, make sure you have updated the .pot files with the 'i18n/extract.py' script in the Learn GDScript app repository.

This script does the following:

- Finds all .po translation files in subdirectories
- Generates msgmerge commands to update each .po file from its .pot template
- Runs all the merge commands to synchronize the translations

This script requires the msgmerge command to be available."""
if "-h" in sys.argv or "--help" in sys.argv:
    print(HELP_TEXT)
    sys.exit(0)

# Ensure msgmerge command is available
try:
    subprocess.check_output(["msgmerge", "--version"])
except subprocess.CalledProcessError:
    print(
        "msgmerge command not found. You need it to synchronize translations.\n"
        "Please install it with 'sudo apt install gettext' and try again.\n"
        "Exiting..."
    )
    exit(1)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
subdirectories = [
    entry
    for entry in os.listdir(THIS_DIR)
    if os.path.isdir(entry) and not (entry.startswith(".") or entry == "images")
]

total_files: int = 0
for subdirectory in subdirectories:
    po_files = [f for f in os.listdir(os.path.join(THIS_DIR, subdirectory)) if f.endswith(".po")]
    total_files += len(po_files)

print(f"Processing {total_files} files...")

total_success: int = 0
total_failed: int = 0
processed_count: int = 0

for subdirectory in subdirectories:
    po_files = [f for f in os.listdir(os.path.join(THIS_DIR, subdirectory)) if f.endswith(".po")]

    for po_file in po_files:
        file_path = os.path.join(THIS_DIR, subdirectory, po_file)

        command = [
            "msgmerge",
            "--update",
            "--backup=none",
            file_path,
            os.path.join(THIS_DIR, po_file.replace(".po", ".pot")),
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            total_success += 1
        except subprocess.CalledProcessError as e:
            print(f"FAILED: {po_file}")
            print(f"Error: {e.stderr}")
            total_failed += 1

        processed_count += 1
        # Updating only every 30 files for performance, this can make a 20% speedup
        if processed_count == total_files or processed_count % max(1, int(total_files / 30)) == 0:
            print(f"\rProcessed {processed_count} / {total_files} files", end="", flush=True)

print("\n")
if total_failed == 0:
    print(f"Success! All {total_files} files were processed successfully.")
else:
    print(f"Completed with some errors:")
    print(f"Successfully processed: {total_success} files")
    print(f"Failed to process: {total_failed} files")
