# Mission 05 — Numbers and Data

## 1. Task / objective
The objective of Mission 5 is to understand digital data representation by manually converting values between decimal, binary, and hexadecimal systems, verifying these calculations using Python built-in functions, building an interactive `number_converter.py` CLI script, and exploring character encoding standards (ASCII and UTF-8).

---

## 2. Work completed

### Task 5.1 — Convert Numbers by Hand

| Question | Your Working and Answer |
|---|---|
| **Convert decimal 13 to binary** | Repeated division by 2:<br>• 13 ÷ 2 = 6, remainder **1**<br>• 6 ÷ 2 = 3, remainder **0**<br>• 3 ÷ 2 = 1, remainder **1**<br>• 1 ÷ 2 = 0, remainder **1**<br>Read remainders bottom-to-top: **1101₂** |
| **Convert decimal 25 to binary** | Repeated division by 2:<br>• 25 ÷ 2 = 12, remainder **1**<br>• 12 ÷ 2 = 6, remainder **0**<br>• 6 ÷ 2 = 3, remainder **0**<br>• 3 ÷ 2 = 1, remainder **1**<br>• 1 ÷ 2 = 0, remainder **1**<br>Read remainders bottom-to-top: **11001₂** |
| **Convert binary 1010 to decimal** | Positional expansion in powers of 2:<br>• (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>• = 8 + 0 + 2 + 0 = **10₁₀** |
| **Convert binary 1101 to decimal** | Positional expansion in powers of 2:<br>• (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)<br>• = 8 + 4 + 0 + 1 = **13₁₀** |
| **Convert hexadecimal A to decimal** | Direct base-16 digit value:<br>• In hexadecimal, digits 10 through 15 are represented by A through F.<br>• A = 10, so (10 × 16⁰) = **10₁₀** |
| **Convert hexadecimal 1F to decimal** | Positional expansion in powers of 16:<br>• (1 × 16¹) + (F × 16⁰)<br>• = (1 × 16) + (15 × 1) = 16 + 15 = **31₁₀** |
| **Convert binary 1111 to hexadecimal** | Group of 4 bits evaluated in decimal:<br>• (1 × 2³) + (1 × 2²) + (1 × 2¹) + (1 × 2⁰) = 8 + 4 + 2 + 1 = 15₁₀<br>• In base 16, 15 is represented by digit **F₁₆** |

---

### Task 5.2 — Verify Using Python

| Conversion Tested | Python Expression Tested | Result | Matches Manual Calculation? |
|---|---|---|---|
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes (matches 1101) |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes (matches 11001) |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes (matches 10) |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes (matches 13) |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes (matches 10) |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes (matches 31) |
| Binary 1111 to hexadecimal | `hex(int("1111", 2))` | `'0xf'` | Yes (matches F) |

---

### Task 5.3 — Build a Small Number Converter
Created and tested `number_converter.py` in `mission-05-numbers-data/`.

#### Test Results:

| Test Number | Binary Output | Hexadecimal Output |
|---|---|---|
| `13` | `0b1101` | `0xd` |
| `42` | `0b101010` | `0x2a` |
| `255` | `0b11111111` | `0xff` |

#### Explanation of Functions:
- `bin(x)`: Converts an integer `x` into a binary string prefixed with `'0b'`.
- `hex(x)`: Converts an integer `x` into a lowercase hexadecimal string prefixed with `'0x'`.
- `int(s, base)`: Parses a numeric string `s` in the specified radix/base into a base-10 Python integer.

---

### Task 5.4 — How is Text Stored?
- **ASCII Decimal Codes**:
  - Uppercase `'A'`: **65** (binary `01000001`)
  - Lowercase `'a'`: **97** (binary `01100001`)
  *(Verified with Python `ord('A')` and `ord('a')`)*.
- **Why Computers Need an Encoding Standard**:
  Digital electronic circuits can only manipulate and store high and low electrical voltages representing binary bits (`0` and `1`). A character encoding standard defines an agreed universal dictionary mapping numeric code points to human-readable glyphs and symbols, guaranteeing that text produced on one system is rendered accurately on any other computer without corruption.
- **Example of a Character Not in Basic ASCII**:
  - The emoji symbol `🚀` (Unicode `U+1F680`) or the Hindi Devanagari letter `अ` (Unicode `U+0905`). Basic 7-bit ASCII only defines 128 characters (English alphabet, digits, common punctuation, control codes). Extended character sets like UTF-8 allow over a million characters, encompassing global scripts and modern symbols.

---

## 3. Commands / tools used
- `python3 -c "..."`: Tested built-in conversion functions interactively.
- `python3 mission-05-numbers-data/number_converter.py`: Executed and validated converter script with multiple test inputs.
- Python built-in functions: `bin()`, `hex()`, `int()`, `ord()`.

## 4. My understanding
- All computer data—numbers, text, images, and audio—is fundamentally encoded as bit streams.
- Hexadecimal is widely used in computing because it acts as a compact, human-readable shorthand for binary, where every 4 bits (nibble) neatly corresponds to a single hexadecimal digit.

## 5. Difficulties faced
- Remembering the conversion value of hex digits past 9 (A=10, B=11, C=12, D=13, E=14, F=15).

## 6. How I resolved them
- Created a quick mental reference chart from 10 to 15 and verified calculations using `int(..., 16)`.

## 7. Evidence / files
- [number_converter.py](number_converter.py)
- [README.md](README.md)

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Gate condition: Ready for staging, commit, and remote push.
