import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True, exclude_ambig=False):
    # 1. Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # 2. Handle Ambiguous Characters (l, 1, I, O, 0)
    if exclude_ambig:
        for char in "l1IO0":
            lowercase = lowercase.replace(char, "")
            uppercase = uppercase.replace(char, "")
            digits = digits.replace(char, "")

    # 3. Build the selection pool and guarantee at least one of each type
    pool = lowercase
    # Initializing the guaranteed list with one lowercase letter
    guaranteed = [secrets.choice(lowercase)] 
    
    if use_upper:
        pool += uppercase
        guaranteed.append(secrets.choice(uppercase))
    if use_digits:
        pool += digits
        guaranteed.append(secrets.choice(digits))
    if use_symbols:
        pool += symbols
        guaranteed.append(secrets.choice(symbols))

    # 4. Fill the rest of the password length
    remaining_length = length - len(guaranteed)
    # Pick randomly from the combined pool for the rest
    password_list = guaranteed + [secrets.choice(pool) for _ in range(remaining_length)]
    
    # 5. Shuffle the list so the guaranteed chars aren't always at the start
    secrets.SystemRandom().shuffle(password_list)
    
    return "".join(password_list)

def check_strength(pw, length, use_upper, use_digits, use_symbols):
    # Simple logic for strength
    score = 0
    if length >= 12: score += 1
    if use_upper: score += 1
    if use_digits: score += 1
    if use_symbols: score += 1
    
    if score <= 2: return "Weak", "red"
    if score == 3: return "Medium", "orange"
    return "Strong", "green"