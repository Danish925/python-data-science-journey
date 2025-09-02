Title
Secure Password Generator (OOP, secrets)

Overview

1.Policy‑driven password generator written in Python with a clean OOP design.

2.Uses the secrets module (OS‑backed CSPRNG) for cryptographically secure randomness, never random.

3.Ensures each password contains at least one character from every enabled class (lower/upper/digits/symbols).

Features

1.OOP structure: PasswordPolicy for configuration, PasswordGenerator for generation.

2.Security: secrets.SystemRandom used for choice and shuffle (unpredictable, suitable for passwords).

3.Coverage: enforces at least one char per enabled class; length must be >= enabled classes.

4.Simple CLI: prompts for length and inclusion of uppercase, digits, symbols; outputs 3 passwords.

Requirements

1.Python 3.9+ (no third‑party dependencies).

Project files

1.main.py: entry point with OOP implementation and interactive CLI.

Quick start

Run:

1.python main.py

Follow the prompts:

1.Length (e.g., 12–20)

2.Include uppercase? (Y/n)

3.Include digits? (Y/n)

4.Include symbols? (Y/n)

Example (library usage)


from main import PasswordPolicy, PasswordGenerator
policy = PasswordPolicy(length=14, use_uppercase=True, use_digits=True, use_symbols=True)
gen = PasswordGenerator(policy)
print(gen.generate_three()) # -> ['sA8!...', '...']


Design notes

1.Why secrets, not random:

secrets draws from the OS cryptographic PRNG; random is deterministic and unsafe for secrets.

2.Validation:

length must be positive and at least the number of enabled classes, guaranteeing diversity.

3.Shuffling:

characters are securely shuffled using SystemRandom to avoid predictable positions.

Security disclaimer

This generator produces strong random passwords but does not manage storage or rotation; integrate with a password manager for persistence and autofill
