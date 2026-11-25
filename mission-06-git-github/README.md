# Mission 06 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to practice the fundamental Git version control workflow (`status`, `add`, `commit`, `log`), work safely with branches (`update-about`), learn how Pull Requests facilitate collaboration on GitHub, and build a clear reference glossary of essential Git commands.

---

## 2. Work completed

### Task 6.1 — Understand the Basic Git Workflow

| Git Operation | What it does in your own words |
|---|---|
| **Check repository status** (`git status`) | Inspects the working tree and staging area to show which branch is active, which files have uncommitted modifications, which are staged for commit, and which are untracked. |
| **Stage selected changes** (`git add <file>`) | Places modified or newly created files into the staging area (index), preparing a curated snapshot of changes to be included in the next commit. |
| **Create a commit** (`git commit -m "<msg>"`) | Permanently records the currently staged snapshot into the local repository's commit history with a descriptive message and unique SHA hash. |
| **View commit history** (`git log`) | Displays the chronological log of recorded commits, showing commit hashes, authors, timestamps, and commit messages. |

#### Difference Between Staging and Committing:
- **Staging (`git add`)** acts like placing items into a shipping box: you can add, remove, or update files in the staging area repeatedly without creating a permanent historical record yet. It lets you select *which specific changes* belong together.
- **Committing (`git commit`)** seals the box and records it permanently into the repository timeline. Once committed, that snapshot is safely stored in Git's version history and can always be referenced or reverted to later.

---

### Task 6.2 — Create and Use a Branch
1. Created a new feature branch named `update-about` using `git checkout -b update-about`.
2. Edited the root `README.md` to add the **"My Learning"** section summarizing concepts mastered across hardware/IPOS, Terminal CLI, operating systems, and binary/hex data representation.
3. Checked `git status`, staged `README.md` with `git add README.md`, and created a dedicated commit (`Add My Learning section to root README on update-about branch`).
4. Switched back to `main` (`git checkout main`) so the `update-about` branch stays isolated and ready to publish to GitHub (`git push -u origin update-about`).

---

### Task 6.3 — Create a Pull Request
- **What is a Branch?**
  A branch is an independent, parallel line of development that diverges from the main codebase (`main`). It allows developers to implement new features, experiments, or documentation edits without risking instability on the main branch.
- **What is a Pull Request (PR)?**
  A Pull Request is a GitHub collaboration proposal asking project maintainers to review changes made on a separate branch (such as `update-about`) and merge them into a target branch (`main`).
- **Why are Branches and PRs Useful in Teamwork?**
  When multiple contributors edit the same repository simultaneously, working on separate branches prevents conflicting edits from breaking the shared main codebase. Pull Requests provide a dedicated space for peer code review, automated checks, inline feedback, and controlled merging before changes become official.
- **Pull Request Status**:
  Branch `update-about` is created locally with commit `e3070fa`. Pending remote push to GitHub to open the Pull Request comparing `update-about` into `main` (and merge upon instructor guidance / review).

---

### Task 6.4 — Git Command Glossary

| Git Operation | Command | One-line explanation in your own words |
|---|---|---|
| **Initialise a repository** | `git init` | Creates a new hidden `.git` directory to start tracking version history in a local folder. |
| **Check status** | `git status` | Shows the current branch along with modified, staged, and untracked files. |
| **Stage changes** | `git add <file>` | Adds modified or new files to the staging index in preparation for a commit. |
| **Commit changes** | `git commit -m "<msg>"` | Saves a permanent snapshot of staged changes to the repository history with an explanatory message. |
| **View history** | `git log` | Lists past commits chronologically with their IDs, authors, dates, and messages. |
| **Create or list branches** | `git branch [name]` | Lists all existing branches when run alone, or creates a new branch when given a name. |
| **Switch branches** | `git checkout <branch>` / `git switch <branch>` | Updates the working directory files to match the selected branch and moves `HEAD` to it. |
| **Publish changes** | `git push [remote] [branch]` | Uploads local branch commits to a remote repository host such as GitHub. |
| **Retrieve remote changes** | `git pull` | Fetches new commits from the remote repository and merges them into the current local branch. |

---

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log --oneline --all --graph`
- `git checkout -b update-about`, `git checkout main`
- Git 2.55.0 & GitHub workflow

## 4. My understanding
- Separating work into atomic commits and feature branches keeps the repository history transparent, reversible, and safe for team collaboration.
- Pull Requests enforce accountability and code quality by allowing changes to be compared side-by-side before entering `main`.

## 5. Difficulties faced
- Ensuring the `update-about` branch stays focused only on the root `README.md` change while continuing mission documentation cleanly on `main`.

## 6. How I resolved them
- Checked out `update-about`, committed only `README.md`, and immediately switched back to `main` via `git checkout main` before documenting Mission 6.

## 7. Evidence / files
- [README.md](README.md) in `mission-06-git-github/`
- Branch `update-about` containing root `README.md` update (`e3070fa`)

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Note on PR status: Branch `update-about` is ready to be pushed to GitHub (`git push -u origin update-about`) to open the PR into `main`.
