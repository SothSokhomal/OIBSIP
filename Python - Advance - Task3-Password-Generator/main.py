import tkinter as tk
from tkinter import messagebox
import pyperclip
from logic import generate_password, check_strength

history = []

# =========================
# COLORS
# =========================
BG = "#F4F7FA"          
CARD = "#FFFFFF"        
CARD_LIGHT = "#E8EEF3" 
TEXT = "#000000"        
MUTED = "#333333"       
ACCENT = "#38BDF8"
ACCENT_HOVER = "#0EA5E9"
SUCCESS = "#16A34A"
BORDER = "#D1D5DB"


# =========================
# FUNCTIONS
# =========================
def on_generate():
    try:
        length = int(length_slider.get())
        u = var_upper.get()
        d = var_digits.get()
        s = var_sym.get()
        a = var_ambig.get()

        pw = generate_password(length, u, d, s, a)

        # Display password
        password_entry.config(show="")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, pw)

        # Copy password
        pyperclip.copy(pw)
        copy_status.config(text="✓ Copied to clipboard", fg=SUCCESS)

        # Strength
        text, color = check_strength(pw, length, u, d, s)
        strength_label.config(text=f"Strength: {text}", fg=color)

        # History
        history.insert(0, pw)

        if len(history) > 5:
            history.pop()

        update_history()

    except Exception as e:
        messagebox.showerror(
            "Generation Error",
            f"An error occurred:\n{str(e)}"
        )


def copy_password():
    password = password_entry.get()

    if password:
        pyperclip.copy(password)
        copy_status.config(
            text="✓ Password copied!",
            fg=SUCCESS
        )
    else:
        copy_status.config(
            text="Generate a password first",
            fg=MUTED
        )


def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="•")
        eye_button.config(text="Show")
    else:
        password_entry.config(show="")
        eye_button.config(text="Hide")


def update_length(value):
    length_value.config(text=f"{int(float(value))} characters")


def update_history():
    for widget in history_frame.winfo_children():
        widget.destroy()

    if not history:
        tk.Label(
            history_frame,
            text="No passwords generated yet",
            bg=CARD,
            fg=MUTED,
            font=("Helvetica", 10)
        ).pack(pady=15)

        return

    for i, password in enumerate(history, start=1):
        row = tk.Frame(
            history_frame,
            bg=CARD_LIGHT,
            height=35
        )
        row.pack(fill="x", pady=3)

        tk.Label(
            row,
            text=f"{i}",
            bg=CARD_LIGHT,
            fg=MUTED,
            font=("Helvetica", 9, "bold"),
            width=3
        ).pack(side="left")

        tk.Label(
            row,
            text=password,
            bg=CARD_LIGHT,
            fg=TEXT,
            font=("Courier", 10),
            anchor="w"
        ).pack(side="left", padx=5)

        def copy_item(pw=password):
            pyperclip.copy(pw)
            copy_status.config(
                text="✓ History password copied",
                fg=SUCCESS
            )

        tk.Button(
            row,
            text="Copy",
            command=copy_item,
            bg=CARD_LIGHT,
            fg=ACCENT,
            activebackground=CARD_LIGHT,
            activeforeground=ACCENT_HOVER,
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            font=("Helvetica", 9, "bold")
        ).pack(side="right", padx=8)


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()

root.title("Secure Password Generator")
root.geometry("520x720")
root.minsize(480, 650)
root.configure(bg=BG)


# =========================
# HEADER
# =========================
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=35, pady=(30, 15))

tk.Label(
    header,
    text="🔐",
    bg=BG,
    fg="#E8EEF3" ,
    font=("Helvetica", 28)
).pack()

tk.Label(
    header,
    text="Secure Password Generator",
    bg=BG,
    fg="#000000",
    font=("Helvetica", 22, "bold")
).pack(pady=(5, 2))

tk.Label(
    header,
    text="Create strong and secure passwords instantly",
    bg=BG,
    fg="#000000",
    font=("Helvetica", 10)
).pack()


# =========================
# SETTINGS CARD
# =========================
settings_card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)
settings_card.pack(fill="x", padx=35, pady=10)

tk.Label(
    settings_card,
    text="PASSWORD SETTINGS",
    bg=CARD,
    fg=ACCENT,
    font=("Helvetica", 9, "bold")
).pack(anchor="w", padx=20, pady=(18, 5))


# Length
length_top = tk.Frame(settings_card, bg=CARD)
length_top.pack(fill="x", padx=20)

tk.Label(
    length_top,
    text="Password Length",
    bg=CARD,
    fg=TEXT,
    font=("Helvetica", 11, "bold")
).pack(side="left")

length_value = tk.Label(
    length_top,
    text="12 characters",
    bg=CARD,
    fg=ACCENT,
    font=("Helvetica", 10, "bold")
)
length_value.pack(side="right")


length_slider = tk.Scale(
    settings_card,
    from_=8,
    to_=32,
    orient="horizontal",
    resolution=1,
    showvalue=False,
    command=update_length,
    bg=CARD,
    fg=TEXT,
    troughcolor=CARD_LIGHT,
    activebackground=ACCENT,
    highlightthickness=0,
    bd=0,
    sliderrelief="flat"
)

length_slider.set(12)
length_slider.pack(fill="x", padx=15, pady=(0, 10))


# =========================
# CHECKBOXES
# =========================
options = tk.Frame(settings_card, bg=CARD)
options.pack(fill="x", padx=20, pady=(5, 15))

var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_sym = tk.BooleanVar(value=True)
var_ambig = tk.BooleanVar(value=False)

checkbox_style = {
    "bg": CARD,
    "fg": TEXT,
    "activebackground": CARD,
    "activeforeground": TEXT,
    "selectcolor": CARD_LIGHT,
    "font": ("Helvetica", 10),
    "cursor": "hand2"
}

tk.Checkbutton(
    options,
    text="Include uppercase",
    variable=var_upper,
    **checkbox_style
).grid(row=0, column=0, sticky="w", pady=5)

tk.Checkbutton(
    options,
    text="Include digits",
    variable=var_digits,
    **checkbox_style
).grid(row=0, column=1, sticky="w", pady=5)

tk.Checkbutton(
    options,
    text="Include symbols",
    variable=var_sym,
    **checkbox_style
).grid(row=1, column=0, sticky="w", pady=5)

tk.Checkbutton(
    options,
    text="Exclude ambiguous",
    variable=var_ambig,
    **checkbox_style
).grid(row=1, column=1, sticky="w", pady=5)


# =========================
# GENERATE BUTTON
# =========================
generate_button = tk.Button(
    root,
    text="⚡  Generate Secure Password",
    command=on_generate,
    bg=ACCENT,
    fg="#0F172A",
    activebackground=ACCENT_HOVER,
    activeforeground="#FFFFFF",
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    font=("Helvetica", 11, "bold"),
    height=2
)

generate_button.pack(fill="x", padx=35, pady=(15, 10))


# =========================
# PASSWORD CARD
# =========================
password_card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)
password_card.pack(fill="x", padx=35, pady=5)

tk.Label(
    password_card,
    text="GENERATED PASSWORD",
    bg=CARD,
    fg=MUTED,
    font=("Helvetica", 9, "bold")
).pack(anchor="w", padx=20, pady=(15, 5))


password_row = tk.Frame(password_card, bg=CARD)
password_row.pack(fill="x", padx=15, pady=(0, 5))

password_entry = tk.Entry(
    password_row,
    font=("Courier", 14, "bold"),
    bg="#0F172A",
    fg="#E8EEF3",
    insertbackground=TEXT,
    relief="flat",
    bd=0,
    justify="center"
)

password_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)

eye_button = tk.Button(
    password_row,
    text="Hide",
    command=toggle_password,
    bg=CARD_LIGHT,
    fg=TEXT,
    activebackground=CARD_LIGHT,
    activeforeground=ACCENT,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    font=("Helvetica", 9, "bold")
)

eye_button.pack(side="right", padx=(8, 0), ipadx=8, ipady=5)


copy_button = tk.Button(
    password_card,
    text="Copy Password",
    command=copy_password,
    bg=CARD_LIGHT,
    fg=TEXT,
    activebackground=BORDER,
    activeforeground=TEXT,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    font=("Helvetica", 10, "bold")
)

copy_button.pack(fill="x", padx=15, pady=(5, 5))


copy_status = tk.Label(
    password_card,
    text="",
    bg=CARD,
    fg=MUTED,
    font=("Helvetica", 9)
)

copy_status.pack(pady=(0, 12))


# =========================
# STRENGTH
# =========================
strength_label = tk.Label(
    root,
    text="Strength: —",
    bg=BG,
    fg=MUTED,
    font=("Helvetica", 12, "bold")
)

strength_label.pack(pady=10)


# =========================
# HISTORY
# =========================
history_title = tk.Frame(root, bg=BG)
history_title.pack(fill="x", padx=35, pady=(5, 5))

tk.Label(
    history_title,
    text="RECENT PASSWORDS",
    bg=BG,
    fg=MUTED,
    font=("Helvetica", 9, "bold")
).pack(side="left")


history_frame = tk.Frame(
    root,
    bg=CARD
)
history_frame.pack(fill="x", padx=35, pady=(0, 20))

update_history()


# =========================
# RUN
# =========================
root.mainloop()


