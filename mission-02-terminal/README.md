# Mission 02 — Become Comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to become proficient with the Unix command-line interface (CLI) in Terminal, practice essential file management commands safely, understand command flags and pipes, and explore the role of package managers.

---

## 2. Work completed

### Task 2.1 — Explore Basic Terminal Operations

| Operation / Command Name | What it does | What I observed |
|---|---|---|
| Current-directory display (`pwd`) | Prints the full absolute path of the current working directory. | Displayed the complete working path (`.../digital-detective-8074`). |
| Directory listing (`ls`) | Lists visible files and directories in the current folder. | Displayed filenames in columns without detailed metadata. |
| Detailed listing (`ls -l`) | Lists files in long format including permissions, owner, size, and date. | Displayed columns for file mode, hard links, owner, group, bytes, and modification timestamp. |
| Change directory (`cd ..` / `cd -`) | Changes the active working directory to parent or previous directory. | Current location changed to parent folder; verified using `pwd`, then navigated back. |
| Create directory (`mkdir <name>`) | Creates a new directory in the file system. | Created folder `terminal-practice` successfully. |
| Create empty file (`touch <file>`) | Creates an empty file or updates access/modification timestamps. | Created `practice.txt` with an initial size of 0 bytes. |
| Copy file (`cp <source> <dest>`) | Creates an identical duplicate of a file under a new destination name. | Produced an exact copy named `practice_backup.txt`. |
| Move / rename file (`mv <old> <new>`) | Moves or renames a file/directory without changing file contents. | Renamed `practice_backup.txt` to `backup_renamed.txt`. |
| Display file contents (`cat <file>`) | Concatenates and outputs full file contents to standard output. | Outputted the written lines of text directly onto the terminal screen. |

---

### Task 2.2 — Practise File Changes Safely
Inside the dedicated `terminal-practice` folder:
1. Created `practice.txt` with an initial line of text using standard redirection (`>`):
   ```bash
   echo "First line: Digital Detective learning." > practice.txt
   ```
2. Appended a second line without overwriting the first using append redirection (`>>`):
   ```bash
   echo "Second line: Appending text using shell redirection." >> practice.txt
   ```
3. Verified both lines using `cat practice.txt`:
   ```text
   First line: Digital Detective learning.
   Second line: Appending text using shell redirection.
   ```
4. Created a backup copy using `cp practice.txt practice_backup.txt` and renamed it using `mv practice_backup.txt backup_renamed.txt`.

#### Conceptual Questions & Answers:
- **What is the difference between replacing a file's contents and adding text to the end?**
  Replacing a file's content (using single `>`) overwrites or truncates the file entirely, destroying previous content. Adding text to the end (using double `>>`) appends new data to the existing file stream without altering existing lines.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) creates an independent duplicate of the file in another location while preserving the original. Moving (`mv`) renames the file or relocates its directory pointer in the filesystem table, leaving only one instance.
- **What information does the current-directory display provide?**
  `pwd` (Print Working Directory) provides the complete absolute path from the root directory (`/`) to the exact folder currently active in the shell session, preventing accidental modifications in incorrect folders.
- **Why is a directory-listing operation useful?**
  Listing (`ls`) allows the user to inspect folder contents, verify that files exist, observe permissions, identify file types, and check file sizes before running scripts or commands.

---

### Task 2.3 — Understand Flags and Pipes
- **Flags Comparison (`ls` vs `ls -lah`)**:
  - `ls`: Displays only bare names of non-hidden files.
  - `ls -lah`:
    - `-l`: Formats output as a long detailed list (permissions, owner, size, timestamp).
    - `-a`: Includes hidden files (entries starting with `.`, like `.git` or `.gitkeep`).
    - `-h`: Formats file sizes in human-readable units (e.g., `B`, `K`, `M`, `G`) instead of raw byte counts.
- **Pipeline Demonstration (`ls -lah terminal-practice | head -n 5`)**:
  - The pipe operator (`|`) takes the Standard Output (`stdout`) of the left command (`ls -lah`) and feeds it directly as the Standard Input (`stdin`) to the right command (`head -n 5`).
  - *Left side (`ls -lah`)* generates the detailed directory listing stream.
  - *Right side (`head -n 5`)* intercepts that stream and truncates output to only display the first 5 lines.

---

### Task 2.4 — Understand Package Managers
- **Installed Package Manager**: Homebrew (`brew`)
- **Version Verified**: Homebrew 7.0.9
- **Command Used**: `brew list` (displays managed packages such as `git`, `node`, `openssl`, `python`, etc.)
- **Why Package Managers are Useful**:
  A package manager automates the fetching, compilation, installation, dependency resolution, and updating of software tools and libraries from centralized repositories. Instead of manually downloading installers, configuring environment paths, and resolving library conflicts, a package manager ensures software integrity and one-command system maintenance.

---

## 3. Commands / tools used
- `pwd`, `cd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `cat`
- Redirection operators: `>` (overwrite) and `>>` (append)
- Pipeline operator: `|` with `head -n 5`
- `brew --version` and `brew list`

## 4. My understanding
- The command line gives precise control over file operations, automation, and script execution without GUI overhead.
- Using flags modifies command functionality, while pipes allow modular composition of simple Unix utilities into powerful data-processing pipelines.

## 5. Difficulties faced
- Remembering whether single `>` or double `>>` is used for appending.

## 6. How I resolved them
- Tested both operators in the `terminal-practice` sandbox directory and confirmed that `>>` safely preserves existing file content.

## 7. Evidence / files
- [README.md](README.md) in `mission-02-terminal/`
- Practice workspace: `terminal-practice/` containing `practice.txt` and `backup_renamed.txt`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Gate condition: Ready for staging, commit, and remote push.
