import os

# The path to the 'cursors' folder
cursors_path = "cursors"

# Make sure the 'cursors' folder exists
os.makedirs(cursors_path, exist_ok=True)

# Create 20 directories inside the 'cursors' folder
for i in range(1, 66):
    dir_path = os.path.join(cursors_path, f"dir{i}")
    os.makedirs(dir_path, exist_ok=True)
