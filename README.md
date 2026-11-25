# Digital Detective

This is an individual SnAI assignment for the Diwali holiday. It is a sequence of missions that investigates how a computer system works — from hardware and software fundamentals to terminal commands, operating-system internals, data encoding, version control with Git, and networking.

## Goal

The main goal of this assignment is to:

- Investigate how your computer works.
- Practise basic Terminal operations.
- Explore how the operating system manages files and programs.
- Understand how numbers and text are represented.
- Use GitHub to publish your work.

## Topics Explored

- IPOS (Input, Processing, Output, Storage) model
- Hardware vs software classification (OS, application, utility)
- Unix Terminal commands, flags, pipes and package managers
- Operating-system responsibilities, processes, paths and permissions
- Compiler vs interpreter comparison
- Decimal ↔ binary ↔ hexadecimal conversions and ASCII / UTF-8 encoding
- Git version control workflow, branches and Pull Requests
- LAN, MAN, WAN, DNS, routers, protocols and client-server architecture

## Mission Index

| S.No. | Folder / File | Purpose |
|------:|---|---|
| 1. | [README.md](README.md) | Assignment introduction, mission index and completion summary. |
| 2. | [mission-00-setup/README.md](mission-00-setup/README.md) | Setup details, tools and repository information. |
| 3. | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) | IPOS, hardware, software and everyday systems. |
| 4. | [mission-02-terminal/README.md](mission-02-terminal/README.md) | Terminal activities and command learning. |
| 5. | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) | OS, processes, paths, storage and permissions. |
| 6. | [mission-04-programs/README.md](mission-04-programs/README.md) | Python test and compiler/interpreter comparison. |
| 7. | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) | Conversions, encoding and converter explanation. |
| 8. | [mission-05-numbers-data/number_converter.py](mission-05-numbers-data/number_converter.py) | Working Python number converter. |
| 9. | [mission-06-git-github/README.md](mission-06-git-github/README.md) | Git workflow, branches and Pull Request learning. |
| 10. | [mission-07-networking/README.md](mission-07-networking/README.md) | Network concepts and observations. |
| 11. | [mission-08-final-report/README.md](mission-08-final-report/README.md) | Final review and submission checklist. |
| 12. | [evidence/](evidence/) | Privacy-safe screenshots or selected output, grouped by mission if needed. |

## How to Run the Number Converter

Navigate to the `mission-05-numbers-data` folder and run:

```bash
python3 mission-05-numbers-data/number_converter.py
```

Enter any decimal integer when prompted. The program displays its binary and hexadecimal equivalents.

**Example output:**
```
Enter a decimal integer: 42
Decimal: 42
Binary: 0b101010
Hexadecimal: 0x2a
```

## What I Learned

- **Computer Fundamentals**: Every computing activity follows the IPOS cycle — raw input is captured by peripherals, processed by the CPU in RAM, presented as output on a display, and retained in persistent storage.
- **Terminal & File Management**: The command line gives precise, scriptable control over files and directories. Flags modify commands; pipes chain simple utilities into powerful workflows.
- **Operating System**: The OS is the core supervisor that manages processes (tracked by PIDs), allocates memory, enforces file permissions (rwx), and provides user interfaces.
- **Programs & Execution**: Compilers translate an entire program ahead of time into a standalone binary; interpreters execute source code line by line at runtime.
- **Data Representation**: All data is stored as binary bits. Hexadecimal provides a compact shorthand (every 4 bits = 1 hex digit). Character encoding standards like ASCII and UTF-8 map numeric codes to human-readable glyphs.
- **Git & GitHub**: Atomic commits and feature branches keep history clean and reversible. Pull Requests enable peer review before merging into `main`.
- **Networking**: The Internet routes packets across LANs, MANs and WANs. DNS translates domain names to IP addresses so browsers can locate servers.

## Note on Submissions

Each mission was completed in sequence and committed separately to the repository. The final report is a summary of all missions and their completion status.
