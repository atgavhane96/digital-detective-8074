# Mission 00 — Setup & Workspace

## 1. Task / objective
The objective of Mission 0 is to create a correctly named project workspace (`digital-detective-8074`), establish the folder and file structure for all subsequent missions, verify that the required development tools (Python 3 and Git) are installed, and prepare the repository for version tracking.

## 2. Work completed
- Checked the installed versions of Python 3 and Git.
- Created the local repository folder named `digital-detective-8074` based on the assignment naming rule.
- Created all required mission folders (`mission-00-setup` through `mission-08-final-report`) and the `evidence/` folder.
- Created initial Markdown `README.md` files in each mission folder and the starter `number_converter.py` in `mission-05-numbers-data/`.
- Authored the root `README.md` containing the project introduction and mission navigation index.

## 3. Commands / tools used
- `python3 --version`: Verified the Python 3 installation (Python 3.14.6).
- `git --version`: Verified the Git installation (git version 2.55.0).
- `mkdir`: Created the mission directory structure.
- `touch`: Created initial `README.md` files and placeholder files.
- `git init`: Initialized the local Git version control repository.
- `git add` & `git commit`: Staged and recorded the initial workspace structure commit.

## 4. My understanding
- **What is a Git repository?**: A repository is a storage space tracked by Git that keeps a complete history of files, directory structures, and code changes over time. It allows developers to revert to previous versions, track changes systematically, and collaborate safely.
- **Why organize by mission?**: Separating the project into mission-specific folders keeps each topic (such as IPOS, terminal commands, operating system concepts, and data encoding) modular and organized. It prevents file clutter in the root directory and makes it easy to review and commit each learning module independently.

## 5. Difficulties faced
- Folders were initially nested within the `evidence/` folder during manual setup.

## 6. How I resolved them
- Used terminal commands (`mv`) to restructure the directories to the project root, matching the assignment specification precisely.

## 7. Evidence / files
- Root `README.md`
- Mission directories: `mission-00-setup/` to `mission-08-final-report/`
- `evidence/.gitkeep`
- `mission-05-numbers-data/number_converter.py`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Status: Ready to commit and push to remote GitHub repository.
