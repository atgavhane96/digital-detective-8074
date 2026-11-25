# Mission 01 — Computer Fundamentals and IPOS

## 1. Task / objective
The objective of Mission 1 is to investigate and explain fundamental computer operations through the IPOS (Input, Processing, Output, Storage) model, classify hardware and software components (operating system, application, and utility), and examine embedded or specialized computer-based systems encountered in everyday life.

---

## 2. Work completed

### Task 1.1 — Trace One Activity Using IPOS
**Chosen Activity**: Searching the web for an article and saving notes locally.

| Stage | What happens in this activity? | Hardware / Component involved |
|---|---|---|
| **Input** | The user types the search query into the browser address bar and clicks the search button. | Keyboard, Mouse / Trackpad |
| **Processing** | The CPU executes browser instructions, handles network sockets, parses HTML/JavaScript, and renders the webpage into memory (RAM). | CPU (Processor), RAM (Memory) |
| **Output** | The rendered webpage and search results are visibly presented to the user on the screen. | Display Screen / Monitor |
| **Storage** | The user saves text notes or downloaded articles to persistent non-volatile storage for future offline access. | SSD (Solid State Drive) / NVMe storage |

**Explanation of Data Flow**:
The activity begins when the user provides raw data via input peripherals (keyboard/trackpad). The operating system and CPU interpret these keystrokes and allocate temporary memory in RAM. After the request is processed and received over the network controller, the CPU renders visual information to the display buffer (output). Finally, when the user explicitly saves the document, the data is transferred from volatile RAM to non-volatile SSD storage.

---

### Task 1.2 — Identify Hardware and Software

| Item / Software Name | Hardware or Software? | Software Type (if applicable) | Purpose |
|---|---|---|---|
| Keyboard | Hardware | Not applicable | Input device used to type alphanumeric characters and execute keyboard shortcuts. |
| Monitor / Retina Display | Hardware | Not applicable | Output peripheral that visually renders user interfaces, text, and graphics. |
| Solid State Drive (SSD) | Hardware | Not applicable | High-speed, non-volatile storage device that permanently retains OS and user files. |
| Central Processing Unit (CPU) | Hardware | Not applicable | The primary processing chip that executes computer instructions and arithmetic calculations. |
| macOS | Software | Operating System | Manages hardware resources, CPU scheduling, memory allocation, and file systems. |
| Visual Studio Code | Software | Application Software | Code editor providing development features such as syntax highlighting and debugging. |
| Google Chrome | Software | Application Software | Web browser used to navigate the internet, render web pages, and run web apps. |
| macOS Activity Monitor / Disk Utility | Software | Utility Software | System utility used to monitor running processes, resource consumption, and disk health. |

---

### Task 1.3 — Computer Systems Around You

| System | Main Purpose | One Input | One Output |
|---|---|---|---|
| Automated Teller Machine (ATM) | Allows bank customers to securely withdraw cash, check balances, and transfer funds. | Numeric PIN keypad / Touchscreen selection / Card chip reader | Cash dispenser / Printed transaction receipt / Display screen |
| Smart Traffic Signal System | Regulates vehicular and pedestrian traffic flow dynamically based on real-time road conditions. | Inductive road loop sensors / Pedestrian crosswalk button / Optical traffic camera | Red, Yellow, Green LED signal lights / Audible pedestrian crossing tone |
| Metro Station Ticket Vending Machine | Enables passengers to select destinations, calculate fares, and purchase transit tokens or reload travel cards. | Interactive destination touch panel / Cash and coin acceptor | Dispensed RFID transit token / Reloaded smart card / Receipt |

---

## 3. Commands / tools used
- Text Editor / Markdown documentation tools.
- Terminal commands to navigate and organize mission documentation.

## 4. My understanding
- **The IPOS Cycle**: Computers are fundamentally data processors. The IPOS framework describes the transformation of raw human interaction (Input) through logical and arithmetic calculation (Processing) into readable results (Output) and persistent retention (Storage).
- **Hardware vs. Software Distinction**: Hardware encompasses the physical circuitry and peripherals that execute electrical signals, while software provides the structured logic and instructions directing the hardware.
- **Software Categories**:
  - *Operating System Software*: Acts as an intermediary bridge between hardware resources and user applications.
  - *Application Software*: Designed to help the end user perform specific productive tasks (browsing, writing, coding).
  - *Utility Software*: Designed for housekeeping, maintenance, diagnosis, and performance optimization of the computer system itself.

## 5. Difficulties faced
- No major difficulties faced during this mission.

## 6. How I resolved them
- Not applicable.

## 7. Evidence / files
- [README.md](README.md) in `mission-01-computer-basics/`

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Gate condition: Ready for staging, commit, and remote push.
