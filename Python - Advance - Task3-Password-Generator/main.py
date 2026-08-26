# import tkinter as tk
# from tkinter import messagebox
# import pyperclip
# from logic import generate_password, check_strength

# history = []

# def on_generate():
#     try:
#         # Get values from GUI
#         length = int(length_slider.get())
#         u = var_upper.get()
#         d = var_digits.get()
#         s = var_sym.get()
#         a = var_ambig.get()

#         # Generate password using the logic file
#         pw = generate_password(length, u, d, s, a)
        
#         # Display the result
#         password_entry.delete(0, tk.END)
#         password_entry.insert(0, pw)
        
#         # Clipboard auto-copy
#         pyperclip.copy(pw)
        
#         # Update Strength Label
#         text, color = check_strength(pw, length, u, d, s)
#         strength_label.config(text=f"Strength: {text}", fg=color)
        
#         # Update History (Show last 5)
#         history.insert(0, pw)
#         if len(history) > 5:
#             history.pop()
#         history_label.config(text="History:\n" + "\n".join(history))
        
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {str(e)}")

# # --- UI Setup ---
# root = tk.Tk()
# root.title("Advanced Password Gen")
# root.geometry("450x600")

# tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold")).pack(pady=20)

# # Length Slider (Added 'length' to fix the UI appearance on Mac)
# tk.Label(root, text="Password Length:", font=("Arial", 10)).pack()
# length_slider = tk.Scale(root, from_=8, to_=32, orient=tk.HORIZONTAL, length=200)
# length_slider.set(12)
# length_slider.pack(pady=5)

# # Checkboxes for features
# var_upper = tk.BooleanVar(value=True)
# var_digits = tk.BooleanVar(value=True)
# var_sym = tk.BooleanVar(value=True)
# var_ambig = tk.BooleanVar(value=False)

# tk.Checkbutton(root, text="Include Uppercase", variable=var_upper).pack(anchor="w", padx=100)
# tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack(anchor="w", padx=100)
# tk.Checkbutton(root, text="Include Symbols", variable=var_sym).pack(anchor="w", padx=100)
# tk.Checkbutton(root, text="Exclude Ambiguous (l, 1, O, 0)", variable=var_ambig).pack(anchor="w", padx=100)

# # Generate Button
# tk.Button(root, text="Generate & Copy", command=on_generate, 
#           bg="#2196F3", fg="black", font=("Arial", 11, "bold"), height=2, width=20).pack(pady=20)

# # Password Display Field
# password_entry = tk.Entry(root, font=("Courier", 14), width=30, justify="center")
# password_entry.pack(pady=5)

# # Strength Indicator
# strength_label = tk.Label(root, text="Strength: -", font=("Arial", 12, "bold"))
# strength_label.pack(pady=10)

# # History Section
# tk.Label(root, text="--- Session History ---", fg="gray").pack(pady=(20, 0))
# history_label = tk.Label(root, text="", fg="gray", font=("Courier", 10), justify="center")
# history_label.pack()

# root.mainloop()


