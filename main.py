import os
import tkinter as tk
from tkinter import filedialog




import tkinter as tk
from tkinter import filedialog

def browse_files():
    file_paths = filedialog.askopenfilenames(initialdir="~", title="Select Files", parent=root)
    if file_paths:
        for file_path in file_paths:
            file_listbox.insert(tk.END, file_path)

root = tk.Tk()
root.title("Easy File Utility")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)

root.geometry(f"{window_width}x{window_height}")

browse_button = tk.Button(root, text="Select Files", command=browse_files)
browse_button.pack()

# move browse button to right end of the window
browse_button.pack(side=tk.TOP, anchor=tk.E, padx=20, pady=20)

# move browse button to right end of the top of window


file_listbox = tk.Listbox(root)
file_listbox.pack(pady=20, fill=tk.BOTH, expand=1)

dir_list = []
file_list = []
for file in os.listdir(os.path.expanduser("~")):
    if os.path.isfile(file):
        file_list.append(file)
    else:
        dir_list.append(file)

dir_list.sort()
file_list.sort()

print(dir_list)
print(file_list)

for e in dir_list:
    file_listbox.insert(tk.END, "DIR: " + e)
for e in file_list:
    file_listbox.insert(tk.END, e)

root.mainloop()









# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.title("Easy File Utility")

# # Get the screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate the window width and height as 50% of the screen size
# window_width = int(screen_width * 0.5)
# window_height = int(screen_height * 0.5)

# root.geometry(f"{window_width}x{window_height}")




# file_paths = filedialog.askopenfilenames()
# if file_paths:
#     for file_path in file_paths:
#         selected_file_label = tk.Label(root, text="Selected File: " + file_path)
#         selected_file_label.pack()

# root.mainloop()













# root = tk.Tk()
# root.title("File Browser")

# # Create the root window
# root = tk.Tk()

# # Get the screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate the window width and height as 50% of the screen size
# window_width = int(screen_width * 0.5)
# window_height = int(screen_height * 0.5)

# root.geometry(f"{window_width}x{window_height}")

# file_path = filedialog.askopenfilename()
# if file_path:
#     selected_file_label = tk.Label(root, text="Selected File: " + file_path)
#     selected_file_label.pack(pady=20)

# root.mainloop()





# # open window showing files in users home directory
# def browse_files():
#     file_path = filedialog.askopenfilename(initialdir="~/", title="Select a File")
#     print("Selected file:", file_path)


# # Create the root window
# root = tk.Tk()

# # Get the screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate the window width and height as 50% of the screen size
# window_width = int(screen_width * 0.5)
# window_height = int(screen_height * 0.5)


# root.title("PYFILE")
# root.geometry(f"{window_width}x{window_height}")
# root.configure(bg="white")
# # root.iconbitmap("icon.ico")

# # create scrollbar
# scrollbar = tk.Scrollbar(root)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # # create a listbox with files in users home directory
# # listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
# # listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
# # listbox.configure(bg="white", fg="black", font=("Arial", 12))
# # scrollbar.config(command=listbox.yview)

# # for file in os.listdir(os.path.expanduser("~")):
# #     if os.path.isfile(file):
# #         listbox.insert(tk.END, file)
# #     else:
# #         listbox.insert(tk.END, f"{file}/")

# # create a button to browse files
# browse_button = tk.Button(root, text="Browse Files", command=browse_files)
# browse_button.pack()





# root.mainloop()
