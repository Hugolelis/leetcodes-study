# LeetCodes

> A personal collection of LeetCode problem solutions in Python, built to practice algorithms and data structures with clean, readable code.

<div align="left">

[![Status](https://img.shields.io/badge/Status-Studying-52719d?style=for-the-badge&labelColor=1a1a1a&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-0f766e?style=for-the-badge&labelColor=1a1a1a&logoColor=white)]()

</div>

<details>
<summary><strong>Table of Contents</strong></summary>

- [About](#about)
- [Solutions](#solutions)
- [Tech Stack](#tech-stack)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Author](#author)
- [License](#license)

</details>

---

## About

This repository is a personal practice log for LeetCode problems, solved in Python. The goal isn't just to pass the test cases. It's deliberate practice: recognizing patterns (two pointers, sliding window, hashing, DP, graph traversal, etc.), reasoning about time/space complexity, and writing solutions that stay readable instead of golfed one-liners. Each problem lives in its own file so it can be run and tested in isolation.

---

## Solutions

<!-- Update this table as problems are added. -->
| Problem | File | Difficulty | Pattern |
|---|---|---|---|
| Two Sum | [challenges/two_sum.py](challenges/two_sum.py) | Easy | Hashing |
| Palindrome Number | [challenges/palindrome_number.py](challenges/palindrome_number.py) | Easy | String Reversal |
| Roman to Integer | [challenges/roman_to_integer.py](challenges/roman_to_integer.py) | Easy | Hashing |
| Valid Parentheses | [challenges/valid_parentheses.py](challenges/valid_parentheses.py) | Easy | Stack |

---

## Tech Stack

- **Language:** Python 3
- **Dependencies:** none (standard library only)
- **Testing:** none yet, see [Known limitations](#architecture--design-decisions)

---

## Architecture & Design Decisions

```
.
├── challenges/
│   ├── two_sum.py
│   ├── palindrome_number.py
│   ├── roman_to_integer.py
│   └── valid_parentheses.py
└── README.md
```

Each file holds one `Solution` class in the LeetCode format, with its time complexity noted in the method's docstring, and a single `print` at the bottom that calls it with a sample input.

**Why this shape:** all solutions live under `challenges/`, one file per problem named after its slug (e.g. `two_sum.py`), keeping the repo root clean and leaving room for future top-level content (notes, tests) without mixing it with solution code. The `Solution` class is kept as LeetCode expects it, so a solution can be pasted into the platform as is.

**Known limitations:**
- No automated tests yet: solutions are only checked by the single sample call at the bottom of each file.
- No CLI or runner script to execute a specific problem by name.
- Four problems solved so far (all Easy); the repo is in its early stages.

---

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone https://github.com/Hugolelis/leetcodes-study.git
cd leetcodes-study
```

No external dependencies: every solution uses only the Python standard library.

---

## Usage

Each file is self-contained. Run it directly with Python and it prints the result of its sample call:

```bash
python3 challenges/two_sum.py
```
```
[0, 1]
```

To try other inputs, edit the `print(...)` line at the bottom of the file.

---

## Author

[Hugolelis](https://github.com/Hugolelis)

---

## License

Distributed under the **MIT License**.
