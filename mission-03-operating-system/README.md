# Mission 03 — Understand the Operating System

## 1. Task / objective
The objective of Mission 3 is to examine the role of the operating system (OS), inspect system information and storage utilization safely from the Terminal, understand processes and process identifiers (PID), analyze filesystem paths and Unix permissions, and explain the core responsibilities of modern operating systems.

---

## 2. Work completed

### Task 3.1 — Explore Your Operating System

| Information Explored | What it tells you | Your Observation (privacy-safe) |
|---|---|---|
| Operating system / system details | Kernel name, OS release version, and machine processor architecture. | `Darwin 27.2.0 arm64` (macOS on 64-bit Apple Silicon architecture). |
| Current account identity | The username of the currently logged-in active terminal user. | `[redacted-student-user]` (verified using `whoami`). |
| Available and used storage | Total storage capacity, used disk space, available space, and filesystem mount point. | Root volume capacity 460 GiB; Used ~13 GiB (4%); Available 328 GiB mounted on `/`. |
| System activity snapshot | Overview of active tasks, CPU usage, memory allocation, and running threads. | Active tasks monitored via system activity snapshot (`top` / Activity Monitor), showing running system daemons and user apps. |

---

### Task 3.2 — Understand Processes
- **What is a process?**
  A process is an active, executing instance of a computer program loaded into RAM, assigned its own memory address space, threads, and system resources managed by the OS kernel.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique numeric integer assigned by the operating system to every running process upon initialization, enabling the OS kernel and users to track, signal, manage, or terminate the process.
- **Two examples of processes running on the computer**:
  1. `zsh` or `bash`: The command-line shell process interpreting terminal commands.
  2. `Google Chrome` (or `Finder`): An application-level user process handling browsing or graphical file management.

---

### Task 3.3 — Understand Paths and Permissions

#### Absolute vs. Relative Paths
- **Absolute Path**: The full, complete directory path starting from the filesystem root (`/`). It points to the exact same file regardless of the current working directory.
  - *Example in assignment*: `/Users/[redacted]/Documents/digital-detective-8074/mission-03-operating-system/README.md`
- **Relative Path**: The path to a file or folder defined in relation to the current working directory.
  - *Example in assignment*: `./terminal-practice/practice.txt` (or `../mission-02-terminal/README.md`)

#### File Permissions Analysis
Examining the practice file using `ls -l terminal-practice/practice.txt`:
```text
-rw-r--r--@ 1 [redacted] staff 93 Nov 25 20:02 terminal-practice/practice.txt
```
The permission string `-rw-r--r--` breaks down as:
- First character `-`: Regular file type.
- Owner permissions `rw-`: The owner has **Read** (`r`) and **Write** (`w`) permissions, but **cannot Execute** (`-`).
- Group permissions `r--`: Members of the group can only **Read** the file.
- Others permissions `r--`: All other users on the system can only **Read** the file.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows the file's contents to be viewed or read into memory. | Viewing or opening a `.txt` file with `cat` or an editor. |
| `w` — Write | Allows modifying, editing, appending to, or deleting the file's contents. | Saving new edits or appending text using `>>`. |
| `x` — Execute | Allows running the file as a program/script; on a directory, allows traversal/entering (`cd`). | Executing a shell script `./deploy.sh` or Python executable. |

---

### Task 3.4 — Explain Operating-System Responsibilities

| OS Responsibility | Your Explanation | Example |
|---|---|---|
| **Process Management** | Schedules CPU time among competing active programs, manages context switching, and ensures fair resource distribution. | Allocating CPU cores so that a web browser, code editor, and music player run concurrently without freezing. |
| **Memory Management** | Allocates, tracks, and protects volatile RAM blocks for active processes and frees memory when applications terminate. | Assigning 200 MB of RAM when opening a Python program and reclaiming that memory when the script finishes. |
| **Device Management** | Interfaces with hardware peripherals using device drivers, translating generic software read/write calls into device-specific signals. | Sending print jobs to a USB/network printer or receiving input coordinates from an external mouse. |
| **File Management** | Organizes, stores, tracks, and retrieves data systematically in folders and files across non-volatile storage drives. | Creating, renaming, and reading files on an APFS/NTFS partition with directory structures and timestamps. |
| **User Interface / Shell** | Provides human users with visual (GUI) or text-based (CLI) environments to interact with and control the system. | The macOS graphical Finder desktop and the Unix `zsh` Terminal prompt. |
| **Security & Permissions** | Enforces user authentication, access control lists (ACLs), privilege separation, and sandboxing to protect sensitive files and processes. | Preventing a standard user program from modifying restricted system root directories (`/System` or `/etc`). |

---

## 3. Commands / tools used
- `uname -srm`: Checked OS kernel name, version, and architecture.
- `whoami`: Checked the active user session identity.
- `df -h /`: Inspected storage usage and available volume space.
- `ls -l`: Inspected file permission flags and ownership.
- `pwd` and `cd`: Tested navigation and verified relative vs. absolute path structures.

## 4. My understanding
- The operating system acts as the core supervisor of the computer, abstracting complex physical hardware into accessible services and interfaces for user software.
- Proper path specifications ensure scripts and programs locate resources reliably, while Unix permission bits (`rwx`) protect data integrity and privacy across multi-user environments.

## 5. Difficulties faced
- Interpreting the three sets of permission bits (`owner`, `group`, `others`).

## 6. How I resolved them
- Broken down `-rw-r--r--` character by character into three 3-tuple segments to confirm owner read/write capabilities clearly.

## 7. Evidence / files
- [README.md](README.md) in `mission-03-operating-system/`

## 8. Commit details
- Commit message: `Document operating system and file management`
- Gate condition: Ready for staging, commit, and remote push.
