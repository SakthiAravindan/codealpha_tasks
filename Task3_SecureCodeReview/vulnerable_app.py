# vulnerable_app.py

import os

def login(username, password):
    # Hardcoded credentials (NOT SAFE)
    if username == "admin" and password == "admin123":
        print("Login successful!")
    else:
        print("Login failed.")

def get_file(filename):
    # No input check (Path Traversal)
    with open(f"./files/{filename}", "r") as f:
        print(f.read())

def run_command(cmd):
    # Runs any system command (VERY DANGEROUS)
    os.system(cmd)

# Try it
login("admin", "admin123")
get_file("../../etc/passwd")
run_command("rm -rf /")
