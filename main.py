import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def select_file():
    global img_path
    img_path = filedialog.askopenfilename(
        filetypes=[("PNG Images", "*.png *.PNG")])
    if img_path:
        label_file.config(text=f"Selected file: {img_path.split('/')[-1]}")

def expand_image():
    if not img_path:
        messagebox.showerror("Error", "Please select an image first.")
        return

    try:
        top = int(entry_top.get())
        bottom = int(entry_bottom.get())
        left = int(entry_left.get())
        right = int(entry_right.get())
    except ValueError:
        messagebox.showerror("Error", "All padding values must be integers.")
        return

    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    new_w = w + left + right
    new_h = h + top + bottom

    new_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))  # Transparent background
    new_img.paste(img, (left, top), mask=img)

    output_path = "output.png"
    new_img.save(output_path)
    messagebox.showinfo("Success", f"Expanded image saved to: {output_path}")

# GUI Setup
root = tk.Tk()
root.title("Transparent Padding Expander")

img_path = ""

# File selection
btn_file = tk.Button(root, text="📂 Choose File", command=select_file)
btn_file.grid(row=0, column=0, columnspan=2, pady=10)

label_file = tk.Label(root, text="No file selected")
label_file.grid(row=1, column=0, columnspan=2, pady=5)

# Padding inputs
tk.Label(root, text="Top Padding (px)").grid(row=2, column=0)
entry_top = tk.Entry(root)
entry_top.insert(0, "50")
entry_top.grid(row=2, column=1)

tk.Label(root, text="Bottom Padding (px)").grid(row=3, column=0)
entry_bottom = tk.Entry(root)
entry_bottom.insert(0, "50")
entry_bottom.grid(row=3, column=1)

tk.Label(root, text="Left Padding (px)").grid(row=4, column=0)
entry_left = tk.Entry(root)
entry_left.insert(0, "50")
entry_left.grid(row=4, column=1)

tk.Label(root, text="Right Padding (px)").grid(row=5, column=0)
entry_right = tk.Entry(root)
entry_right.insert(0, "50")
entry_right.grid(row=5, column=1)

# Expand button
btn_expand = tk.Button(root, text="Expand", command=expand_image)
btn_expand.grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()

