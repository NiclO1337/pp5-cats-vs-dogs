import os
current_dir = os.getcwd()
print(current_dir)
os.chdir(os.path.dirname(current_dir))
print("You set a new current directory")
current_dir = os.getcwd()
print(current_dir)