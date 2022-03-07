import os
import subprocess


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
commands = []
for subdirectory in subdirectories:
    for po_file in os.listdir(os.path.join(THIS_DIR, subdirectory)):
        file_path = os.path.join(THIS_DIR, subdirectory, po_file)
        if not po_file.endswith(".po"):
            raise Exception(
                "Unexpected file in translations directory: {}".format(file_path)
            )
        command = [
            "msgmerge",
            "--update",
            "--backup=none",
            file_path,
            os.path.join(THIS_DIR, po_file.replace(".po", ".pot")),
        ]
        commands.append(command)

for command in commands:
    subprocess.run(command)
