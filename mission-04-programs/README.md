# Mission 04 — How Programs Run

## 1. Task / objective
The objective of Mission 4 is to write and execute a basic Python 3 script from the Terminal (`hello.py`) and compare how compilers and interpreters translate and execute source code.

---

## 2. Work completed

### Task 4.1 — Create and Run a Python Program
Created `hello.py` inside `mission-04-programs/` with the following one-line program:
```python
print("Hello from Python")
```
Executed the script from Terminal using:
```bash
python3 mission-04-programs/hello.py
```
**Observed Output**:
```text
Hello from Python
```

---

### Task 4.2 — Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation / execution happens** | Translates the entire source code program at once *before* execution begins (ahead-of-time). | Translates and executes source code line by line (or statement by statement) *at runtime*. |
| **Typical output** | Produces a standalone machine-code executable binary file (e.g., `.exe`, `a.out`) or intermediate object code. | Does not save a separate machine-code executable; immediately outputs program execution results or runtime errors. |
| **One example** | C / C++ (`gcc`, `clang`), Rust (`rustc`), Go. | Python (`python3`), Ruby, Bash / Zsh shell scripts. |
| **One advantage** | Compiled binaries run much faster at execution time because translation is already complete and optimized. | Easier and faster to debug and test interactively since errors are caught line-by-line without waiting for a full compile step. |

#### Difference Between a Compiler and an Interpreter
As summarized in the table, the primary difference between a compiler and an interpreter lies in *when* and *how* source code is translated for the CPU. A compiler processes the entire source code upfront into an optimized standalone executable binary, which makes the final running program faster but requires a separate build step before running. In contrast, an interpreter reads and executes instructions directly during runtime line by line, eliminating the pre-compilation step and allowing quick testing and cross-platform portability, though usually at slower execution speeds. Modern programming runtimes like standard Python (CPython) even blend both ideas by compiling source code into internal bytecode before an interpreter virtual machine executes it.

---

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Runs the Python 3 interpreter to execute the script.
- Text editor / Python 3.14.6 runtime.

## 4. My understanding
- Computers only execute binary machine instructions directly on the CPU, so human-readable high-level code must always be translated.
- Interpreted languages like Python prioritize rapid development, readability, and immediate execution feedback, whereas compiled languages prioritize raw runtime performance and standalone binary deployment.

## 5. Difficulties faced
- No major difficulties faced during this mission.

## 6. How I resolved them
- Not applicable.

## 7. Evidence / files
- [hello.py](hello.py)
- [README.md](README.md)

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Gate condition: Ready for staging, commit, and remote push.
