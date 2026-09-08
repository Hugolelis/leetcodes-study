# LeetCodes

> A personal collection of LeetCode problem solutions in Python, built to practice algorithms and data structures with clean, readable code.

<div align="left">

[![License](https://img.shields.io/badge/License-MIT-1a1a2e?style=for-the-badge&logoColor=white)](LICENSE)
[![Language](https://img.shields.io/badge/Language-Python-1a1a2e?style=for-the-badge&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-In%20Development-1a1a2e?style=for-the-badge&logoColor=white)]()

</div>

<details>
<summary><strong>Table of Contents</strong></summary>

- [About](#about)
- [Solutions](#solutions)
- [Tech Stack](#tech-stack)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

</details>

---

## About

This repository is a personal practice log for LeetCode problems, solved in Python. The goal isn't just to pass the test cases — it's deliberate practice: recognizing patterns (two pointers, sliding window, hashing, DP, graph traversal, etc.), reasoning about time/space complexity, and writing solutions that stay readable instead of golfed one-liners. Each problem lives in its own file so it can be run and tested in isolation.

---

## Solutions

<!-- Update this table as problems are added. -->
| Problem | File | Difficulty | Pattern |
|---|---|---|---|
| Two Sum | [challenges/two_sum.py](challenges/two_sum.py) | Easy | Hashing |

---

## Tech Stack

- **Language:** Python 3
- **Testing:** none yet — see [Known limitations](#architecture--design-decisions)

---

## Architecture & Design Decisions

```
.
├── challenges/
│   └── two_sum.py
└── README.md
```

**Why this shape:** all solutions live under `challenges/`, one file per problem named after its slug (e.g. `two_sum.py`), keeping the repo root clean and leaving room for future top-level content (notes, tests) without mixing it with solution code.

**Known limitations:**
- No automated tests yet — solutions aren't verified against edge cases beyond manual checks.
- No CLI or runner script to execute a specific problem by name.
- Only one problem solved so far; the repo is in its early stages.

---

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone https://github.com/hugolelis/leetcodes.git
cd leetcodes
```

No external dependencies — every solution uses only the Python standard library.

---

## Usage

Each file is self-contained. Run it directly with Python:

```bash
python3 challenges/two_sum.py
```

---

## License

Distributed under the **MIT License**.

---

## Author

**Hugo** — [GitHub](https://github.com/hugolelis)
