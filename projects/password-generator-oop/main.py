"""
Secure Password Generator (OOP, secrets)

Generates strong passwords using cryptographically secure randomness.
Users select length and inclusion of uppercase, digits, and symbols
(lowercase is always included). The generator guarantees at least one
character from every enabled class and returns three passwords per run.

Security notes:
- Uses secrets.SystemRandom for OS-backed CSPRNG.
- Avoids the non-cryptographic random module for any selection or shuffle.
"""

from dataclasses import dataclass
from typing import List
import secrets
import string


@dataclass
class PasswordPolicy:
    """Configuration for password generation.

    Attributes:
        length: Target password length; must be positive.
        use_lowercase: Include lowercase letters.
        use_uppercase: Include uppercase letters.
        use_digits: Include decimal digits.
        use_symbols: Include punctuation symbols.
    """
    length: int = 12
    use_lowercase: bool = True
    use_uppercase: bool = True
    use_digits: bool = True
    use_symbols: bool = True

    def validate(self) -> None:
        """Validate internal consistency and feasibility.

        Raises:
            ValueError: If length <= 0 or length is less than the number of
                enabled character classes (cannot satisfy “at least one per class”).
        """
        if self.length <= 0:
            raise ValueError("length must be positive")
        enabled_classes = sum([
            self.use_lowercase,
            self.use_uppercase,
            self.use_digits,
            self.use_symbols,
        ])
        if self.length < enabled_classes:
            raise ValueError(
                f"length must be >= {enabled_classes} to include one from each enabled class"
            )


class PasswordGenerator:
    """Secure password generator enforcing a PasswordPolicy.

    The generator:
      - Builds the allowed character pool from policy flags.
      - Ensures coverage: at least one char from each enabled class.
      - Fills remaining length from the whole pool.
      - Shuffles positions via a cryptographically secure PRNG.

    Example:
        policy = PasswordPolicy(length=14, use_uppercase=True, use_digits=True, use_symbols=True)
        gen = PasswordGenerator(policy)
        passwords = gen.generate_three()
    """

    def __init__(self, policy: PasswordPolicy) -> None:
        """Initialize with a validated policy and prepare character sets.

        Args:
            policy: The generation policy to enforce.

        Raises:
            ValueError: If policy is invalid or no character classes are enabled.
        """
        self.policy = policy
        self.policy.validate()

        # OS-backed CSPRNG for both choice and shuffle (security-critical).
        self._rand = secrets.SystemRandom()

        # Assemble per-class sets as strings; disable by emptying.
        self._lower = string.ascii_lowercase if self.policy.use_lowercase else ""
        self._upper = string.ascii_uppercase if self.policy.use_uppercase else ""
        self._digits = string.digits if self.policy.use_digits else ""
        self._symbols = string.punctuation if self.policy.use_symbols else ""

        # Global pool for general draws.
        self._pool = "".join([self._lower, self._upper, self._digits, self._symbols])
        if not self._pool:
            raise ValueError("No character classes enabled")

    def generate_one(self) -> str:
        """Generate a single password satisfying the policy.

        Process:
            1) One required character from each enabled class.
            2) Remaining characters from the full pool.
            3) Secure shuffle to randomize positions.

        Returns:
            A password of length == policy.length.
        """
        required: List[str] = []

        if self._lower:
            required.append(self._rand.choice(self._lower))
        if self._upper:
            required.append(self._rand.choice(self._upper))
        if self._digits:
            required.append(self._rand.choice(self._digits))
        if self._symbols:
            required.append(self._rand.choice(self._symbols))

        remaining = max(0, self.policy.length - len(required))
        tail = [self._rand.choice(self._pool) for _ in range(remaining)]

        chars = required + tail
        self._rand.shuffle(chars)  # secure, unbiased permutation
        return "".join(chars)

    def generate_three(self) -> List[str]:
        """Generate exactly three passwords.

        Returns:
            A list with three independently generated passwords.
        """
        return [self.generate_one() for _ in range(3)]


def _prompt_bool(msg: str, default: bool) -> bool:
    """Prompt for a boolean (yes/no) with a default.

    Args:
        msg: Prompt text.
        default: Value used on empty input.

    Returns:
        True if input is affirmative; False otherwise.
    """
    suffix = "Y/n" if default else "y/N"
    ans = input(f"{msg} ({suffix}): ").strip().lower()
    if not ans:
        return default
    return ans in ("y", "yes", "true", "1")


def _prompt_int(msg: str, default: int) -> int:
    """Prompt for a positive integer with a default fallback.

    Args:
        msg: Prompt text.
        default: Value used on empty/invalid input.

    Returns:
        A positive integer.
    """
    ans = input(f"{msg} [{default}]: ").strip()
    if not ans:
        return default
    try:
        val = int(ans)
        if val <= 0:
            raise ValueError
        return val
    except ValueError:
        print("Please enter a positive integer. Using default.")
        return default


def main() -> None:
    """Interactive entry point."""
    print("Secure Password Generator (OOP, secrets)")

    length = _prompt_int("Password length", 12)
    use_upper = _prompt_bool("Include uppercase", True)
    use_digits = _prompt_bool("Include digits", True)
    use_symbols = _prompt_bool("Include symbols", True)

    policy = PasswordPolicy(
        length=length,
        use_lowercase=True,   # baseline alphabet included by default
        use_uppercase=use_upper,
        use_digits=use_digits,
        use_symbols=use_symbols,
    )

    try:
        gen = PasswordGenerator(policy)
        pwds = gen.generate_three()
        print("\nGenerated passwords:")
        for i, p in enumerate(pwds, start=1):
            print(f"{i}. {p}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
