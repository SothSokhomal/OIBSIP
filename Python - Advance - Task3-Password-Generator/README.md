# Task 3: Advanced Random Password Generator
**Internship:** Oasis Infobyte (OIBSIP)  
**Track:** Python Development  
**Level:** Advanced Tier  

## 📌 Project Overview
This project is a cryptographically secure Password Generator built with a graphical user interface (GUI). Unlike standard generators that use the `random` module, this tool utilizes the `secrets` module to ensure passwords are secure enough for real-world use. 

It features a customizable length slider, character type toggles, a strength indicator, and an automatic generation history.

## ✨ Features
- **Secure Generation:** Uses the `secrets` module for high-entropy randomness.
- **Strict Enforcement:** Guarantees at least one character from every selected category (Uppercase, Lowercase, Numbers, Symbols) is included.
- **Ambiguous Character Filtering:** Optional removal of confusing characters (e.g., `l, 1, I, o, 0, O`).
- **Dynamic Strength Indicator:** Visual feedback (Red/Yellow/Green) based on password complexity and length.
- **Clipboard Integration:** Automatic copying to clipboard using `pyperclip`.
- **Session History:** Displays the last 5 passwords generated in the current session.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **GUI Library:** `tkinter`
- **Security:** `secrets`, `string`
- **Clipboard Management:** `pyperclip`

## 🧠 Logic & Implementation
### 1. The Logic (`logic.py`)
- **Character Sets:** Defined using `string.ascii_letters`, `string.digits`, and `string.punctuation`.
- **Filtering:** A function cleans the character sets if the "Exclude Ambiguous" option is selected.
- **Enforcement:** The generator uses a `while True` loop to verify that the generated string contains at least one character from each selected set.

### 2. Strength Calculation
- **Weak:** Length < 8 OR only 1 character type.
- **Medium:** Length 8-12 AND 2 character types.
- **Strong:** Length > 12 AND 3+ character types.

## 🚀 How to Run
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/OIBSIP.git
   cd OIBSIP/Python-Task3-RandomPasswordGenerator