# CFT — Computer Fundamentals and Technology | CAE-1 Study Notes

**Units per standard NEP 2020 pattern — verify against class notes, since the official 2026-27 scheme is not published.**

---

## Unit 1: Computer Fundamentals

### Topic list
- Definition and characteristics of computers
- History and generations of computers
- Types of computers
- Basic organization of a digital computer (CPU: ALU + CU, memory, input/output)
- Number systems: binary, octal, decimal, hexadecimal + conversions
- Computer codes: BCD, ASCII, Unicode
- Boolean algebra basics: operators and truth tables

### 1.1 Definition and characteristics

**Computer** = an electronic device that accepts data (input), processes it according to instructions, and produces meaningful results (output). It follows the **IPO cycle**: Input → Process → Output.

**Characteristics of computers:**
| Characteristic | Meaning |
|---|---|
| **Speed** | Executes millions/billions of operations per second (measured in MIPS, GHz) |
| **Accuracy** | Results are 100% correct if the input and program are correct |
| **Diligence** | Never gets tired or bored; performs repetitive tasks without loss of quality |
| **Versatility** | Can perform many different tasks (calculations, gaming, editing, browsing) |
| **Storage** | Can store huge amounts of data for a long time |
| **No IQ** | Has no intelligence of its own; only follows given instructions (GIGO) |
| **No feelings** | No emotions or judgement; works purely on logic |

**GIGO** = Garbage In, Garbage Out: wrong input gives wrong output, even though processing was correct.

### 1.2 History and generations of computers

| Generation | Period | Key technology | Example |
|---|---|---|---|
| **1st** | 1940–56 | Vacuum tubes | ENIAC, UNIVAC, IBM 701 |
| **2nd** | 1956–63 | Transistors | IBM 7090, PDP-1 |
| **3rd** | 1964–71 | Integrated Circuits (ICs) | IBM 360 |
| **4th** | 1971–present | Microprocessors (VLSI) | PCs, laptops, Intel 4004 |
| **5th** | Present–future | AI, ULSI, parallel processing | Robots, voice assistants |

Key point for exams: each generation changed the **switching element** (tube → transistor → IC → microprocessor → AI).

### 1.3 Types of computers

- **By purpose:** Analog (measures continuous data, e.g. speedometer), Digital (works on discrete 0/1 data — most computers), Hybrid (mix of both, e.g. hospital ICU monitors).
- **By size/capacity:** Microcomputer (PCs, laptops), Minicomputer (mid-range, small companies), Mainframe (large organizations, banks), Supercomputer (fastest, weather forecasting, research — e.g. PARAM).

### 1.4 Basic organization of a digital computer (block diagram)

```
  ┌────────┐   ┌────────────┐   ┌────────┐
  │ Input  │ → │    CPU     │ → │ Output │
  └────────┘   │ ┌────┐     │   └────────┘
               │ │ CU │     │   ┌────────┐
               │ ├────┤     │ ↔ │ Memory │
               │ │ALU │     │   └────────┘
               │ └────┘     │
               └────────────┘
```

- **Input unit:** feeds data/instructions in (keyboard, mouse, scanner).
- **CPU (Central Processing Unit):** the "brain". Two parts:
  - **ALU (Arithmetic Logic Unit):** does all arithmetic (+, −, ×, ÷) and logical (AND, OR, NOT, comparisons) operations.
  - **CU (Control Unit):** coordinates everything; fetches instructions, decodes them, directs data flow. Does NOT process data itself.
- **Memory unit:** stores data, instructions, and results (RAM/ROM).
- **Output unit:** presents results (monitor, printer, speaker).

### 1.5 Number systems and conversions

| System | Base | Digits used |
|---|---|---|
| Binary | 2 | 0, 1 |
| Octal | 8 | 0–7 |
| Decimal | 10 | 0–9 |
| Hexadecimal | 16 | 0–9, A–F (A=10 … F=15) |

**Worked examples:**

1. Binary → Decimal: (1011)₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = **13**
2. Decimal → Binary: 13 → divide by 2 repeatedly: 13→6 r**1**, 6→3 r**0**, 3→1 r**1**, 1→0 r**1** → read remainders bottom-up = **(1101)₂**
3. Decimal → Octal: (156)₁₀ → 156÷8=19 r**4**, 19÷8=2 r**3**, 2÷8=0 r**2** → **(234)₈**
4. Decimal → Hex: (255)₁₀ → 255÷16=15 r**15(F)**, 15÷16=0 r**15(F)** → **(FF)₁₆**
5. Binary → Octal: group in 3s from right: (101101)₂ → 101|101 = 5|5 = **(55)₈**
6. Binary → Hex: group in 4s: (10110111)₂ → 1011|0111 = B|7 = **(B7)₁₆**
7. Octal → Binary: expand each digit to 3 bits: (53)₈ = 101|011 = **(101011)₂**
8. Hex → Binary: expand each digit to 4 bits: (A5)₁₆ = 1010|0101 = **(10100101)₂**
9. Fractional decimal → binary: 0.625 × 2 = 1.25 → 1; 0.25 × 2 = 0.5 → 0; 0.5 × 2 = 1.0 → 1 → **(0.101)₂**

Trick: shortcut via binary — decimal→octal/hex is easiest by first converting to binary, then grouping.

### 1.6 Computer codes

- **BCD (Binary Coded Decimal):** each decimal digit written as a 4-bit binary code. E.g. 25 → 0010|0101. Used in calculators/displays.
- **ASCII (American Standard Code for Information Interchange):** 7-bit code (128 characters) — digits, letters, symbols. E.g. 'A' = 65, 'a' = 97, '0' = 48. Extended ASCII uses 8 bits (256 characters).
- **Unicode:** universal standard covering all world languages; UTF-8/UTF-16 encodings; supports lakhs of characters (e.g. Devanagari, emoji).

| Code | Bits | Characters | Use |
|---|---|---|---|
| BCD | 4 per digit | 0–9 | Calculators, digital displays |
| ASCII | 7 (128) / 8 (256) | English text + symbols | Basic text |
| Unicode | 16+ (up to 1M+) | All world scripts | Multilingual text, emoji |

### 1.7 Boolean algebra basics

Variables take only two values: **0 (false)** or **1 (true)**. Basic operators:

- **AND (·):** output 1 only if ALL inputs are 1
- **OR (+):** output 1 if ANY input is 1
- **NOT (′):** inverts the input

**Truth tables:**

AND:
| A | B | A·B |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

OR:
| A | B | A+B |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

NOT:
| A | A′ |
|---|----|
| 0 | 1 |
| 1 | 0 |

**Key Boolean laws:** A+0=A, A·1=A, A+1=1, A·0=0, A+A′=1, A·A′=0, (A′)′=A. **De Morgan's laws:** (A·B)′ = A′+B′, (A+B)′ = A′·B′.

### Unit 1 — likely exam questions

**Q1. Define a computer and explain any four characteristics of a computer.**
Model answer: A computer is an electronic device that accepts data as input, processes it per instructions, and gives meaningful output. Characteristics: (1) **Speed** — millions of operations per second; (2) **Accuracy** — error-free output for correct input/program; (3) **Diligence** — works tirelessly without losing quality; (4) **No IQ** — follows only given instructions, hence GIGO (Garbage In, Garbage Out).

**Q2. Describe the generations of computers with the technology used in each.**
Model answer: 1st (1940–56): vacuum tubes — ENIAC; 2nd (1956–63): transistors — IBM 7090; 3rd (1964–71): integrated circuits — IBM 360; 4th (1971–present): microprocessors/VLSI — PCs; 5th (present–future): AI, parallel processing. Each generation is defined by its switching technology, getting smaller, faster, cheaper.

**Q3. Draw and explain the block diagram of a digital computer.**
Model answer: Draw Input → CPU → Output with Memory connected to CPU (see §1.4). Input unit feeds data; CPU has ALU (arithmetic/logic operations) and CU (fetches, decodes, coordinates — does not process data itself); memory stores data/instructions/results; output unit presents results.

**Q4. Convert: (a) (101101)₂ to decimal and octal; (b) (FF)₁₆ to binary; (c) (156)₁₀ to binary.**
Model answer: (a) Decimal: 32+0+8+4+0+1 = 45; Octal: group 101|101 = (55)₈. (b) F=1111 → (11111111)₂. (c) 156 → 128+16+8+4 → (10011100)₂.

**Q5. Differentiate between BCD, ASCII and Unicode.**
Model answer: BCD uses 4 bits per decimal digit (0–9), used in calculators. ASCII is a 7/8-bit code for 128/256 English characters and symbols. Unicode is a universal multilingual standard supporting 1M+ characters (UTF-8/UTF-16), used for all world scripts and emoji.

**Q6. What are the basic Boolean operators? Give truth tables for AND, OR and NOT.**
Model answer: AND (output 1 only if all inputs 1), OR (output 1 if any input 1), NOT (inverts input). Write the three truth tables from §1.7.

**Q7. State and explain De Morgan's laws with truth tables.**
Model answer: (A·B)′ = A′+B′ and (A+B)′ = A′·B′ — "break the line, change the sign." Verify with a 4-row truth table showing both sides equal for all A, B.

---

## Unit 2: Software, Operating Systems & Memory

### Topic list
- Types of software: system, application, utility
- Computer languages: machine, assembly, high level
- Translators: assembler, compiler, interpreter
- Operating system: functions, features, types
- Memory: primary vs secondary, memory hierarchy
- Input and output devices

### 2.1 Types of software

**Software** = set of programs/instructions that tell hardware what to do.

| Type | Purpose | Examples |
|---|---|---|
| **System software** | Manages hardware, provides platform for other software | OS (Windows, Linux), device drivers |
| **Application software** | Does specific user tasks | MS Word, Chrome, games, Photoshop |
| **Utility software** | Maintenance/housekeeping tasks | Antivirus, disk cleanup, backup tools, WinRAR |

### 2.2 Computer languages

| Level | Language | Features |
|---|---|---|
| **Low level — Machine** | Binary (0s and 1s) | Directly executed by CPU; fastest; machine-dependent; hard to write/debug |
| **Low level — Assembly** | Mnemonics (ADD, MOV, SUB) | Needs an **assembler**; easier than machine code; still machine-dependent |
| **High level** | English-like (C, Python, Java) | Needs **compiler/interpreter**; machine-independent; easy to learn, portable |

### 2.3 Translators

- **Assembler:** converts assembly language → machine code.
- **Compiler:** converts the **entire** high-level program to machine code at once, then executes. Faster execution; errors shown after full scan. (C, C++)
- **Interpreter:** converts and executes **line by line**. Slower execution; easier debugging (error reported immediately). (Python, BASIC)

| Compiler | Interpreter |
|---|---|
| Translates whole program at once | Translates line by line |
| Faster execution | Slower execution |
| Errors listed after full scan | Stops at first error |
| Produces object/exe file | No intermediate file |
| Eg: C, C++ | Eg: Python |

### 2.4 Operating system

**OS** = system software that acts as an **interface between user and hardware**, managing all resources.

**Functions of OS:** process management, memory management, file management, device management (I/O), security and access control, user interface (GUI/CLI).

**Features:** multitasking, timesharing, resource sharing, error handling, convenient interface.

**Types of OS:**
- **Batch OS:** jobs collected in batches, no user interaction (payroll processing).
- **Time-sharing:** CPU time divided among users; each feels sole access (Unix).
- **Real-time OS (RTOS):** responds within strict deadlines (air-traffic control, medical devices).
- **Distributed OS:** many machines work as one (cluster computing).
- **Network OS:** manages network resources (servers).
- **Mobile OS:** for phones/tablets (Android, iOS).

### 2.5 Memory

**Primary memory** (main memory): directly accessed by CPU; fast; volatile (except ROM); limited capacity.
- **RAM:** volatile, read/write, working memory.
- **ROM:** non-volatile, stores startup instructions (BIOS/firmware).
- **Cache:** very fast small memory between CPU and RAM.

**Secondary memory:** permanent storage; slower; non-volatile; large capacity. HDD, SSD, pen drive, CD/DVD, memory card.

| Primary memory | Secondary memory |
|---|---|
| Directly accessed by CPU | Accessed via I/O operations |
| Fast, expensive | Slower, cheaper per GB |
| Volatile (RAM) | Non-volatile |
| Small capacity | Large capacity |
| Eg: RAM, ROM, cache | Eg: HDD, SSD, pen drive |

**Memory hierarchy** (fastest → slowest, smallest → largest): Registers → Cache → RAM → SSD/HDD → Optical/USB → Tape/cloud archive.

### 2.6 Input and output devices

- **Input:** keyboard, mouse, scanner, microphone, webcam, touch screen, joystick, OMR/OCR/MICR readers.
- **Output:** monitor, printer (impact: dot-matrix; non-impact: inkjet, laser), speaker, projector, plotter.
- **Both:** touch screen, modem.

### Unit 2 — likely exam questions

**Q1. Explain the three types of software with examples.**
Model answer: System software manages hardware and provides a platform (OS, device drivers); application software performs specific user tasks (MS Word, browsers, games); utility software does maintenance (antivirus, backup, disk cleanup).

**Q2. Differentiate between machine language, assembly language and high-level language.**
Model answer: Machine language is binary, directly executed, fastest but machine-dependent and hard to write. Assembly uses mnemonics, needs an assembler, still machine-dependent. High-level languages (C, Python) are English-like, portable, machine-independent, but need a compiler/interpreter.

**Q3. Differentiate between compiler and interpreter.**
Model answer: Compiler translates the whole program at once and produces an executable; faster at runtime, errors shown after full scan (C, C++). Interpreter translates and executes line by line; slower, but errors are caught immediately and debugging is easier (Python). Table from §2.3.

**Q4. What is an operating system? Explain its functions.**
Model answer: OS is system software acting as interface between user and hardware. Functions: process management, memory management, file management, device/I/O management, security, and providing a user interface.

**Q5. Explain the types of operating systems with one example each.**
Model answer: Batch (payroll jobs), time-sharing (Unix), real-time/RTOS (air-traffic control), distributed (clusters), network (server OS), mobile (Android, iOS). One line each on how CPU/user interaction differs.

**Q6. Differentiate between primary and secondary memory.**
Model answer: Primary is directly accessed by CPU, fast, expensive, small, volatile (RAM, ROM, cache); secondary is permanent, slower, cheap per GB, large, accessed via I/O (HDD, SSD, pen drive). Table from §2.5.

**Q7. Explain the memory hierarchy with a diagram.**
Model answer: Draw pyramid: Registers (top, fastest/smallest) → Cache → RAM → SSD/HDD → optical/USB → tape/cloud (bottom, slowest/largest). Speed and cost per bit decrease downward; capacity increases downward.

**Q8. List input and output devices. What is the difference between impact and non-impact printers?**
Model answer: Input: keyboard, mouse, scanner, mic. Output: monitor, printer, speaker. Impact printers strike the paper (dot-matrix, noisy, cheap multi-copy); non-impact printers don't touch paper (inkjet, laser — quieter, better quality).

---

## Unit 3: Office Tools, Internet & Emerging Technologies

### Topic list
- MS Office basics: Word, Excel, PowerPoint
- Computer networks and internet basics
- Email and web browsers
- Emerging technologies: AI, IoT, cloud computing, cybersecurity basics

### 3.1 MS Office basics

| Tool | Used for | Key features |
|---|---|---|
| **MS Word** | Word processing (documents) | Formatting, tables, mail merge, spell check; files: .docx |
| **MS Excel** | Spreadsheets (data + calculations) | Formulas, functions (SUM, AVERAGE), charts, pivot tables; files: .xlsx; cell address like B5 |
| **MS PowerPoint** | Presentations (slides) | Slides, themes, animations, transitions, slide show; files: .pptx |

One-liners: Word = documents, Excel = numbers/calculations, PowerPoint = slides. A **workbook** contains worksheets; a **cell** is the intersection of a row and column; a **formula** starts with `=`.

### 3.2 Computer networks and internet basics

**Network** = group of connected computers/devices sharing resources.

| Type | Full form | Range |
|---|---|---|
| **LAN** | Local Area Network | Room/building/campus |
| **MAN** | Metropolitan Area Network | City |
| **WAN** | Wide Area Network | Country/world (internet is the largest WAN) |

**Topologies** (layout of connections): bus, star (most common — all nodes connect to a central hub/switch), ring, mesh, tree.

**Internet basics:** global network of networks using **TCP/IP** protocol. **IP address** = unique numeric address of a device (e.g. 192.168.1.1). **URL** = web address (e.g. https://example.com). **ISP** = Internet Service Provider. **Modem/router** connect a LAN to the internet.

### 3.3 Email and web browsers

**Email:** electronic mail; address format `username@domain.com`. Components: To, Cc, Bcc, Subject, body, attachments. Protocols: **SMTP** (sending), **POP3/IMAP** (receiving).

**Web browser:** software to access the web — Chrome, Firefox, Edge, Safari. A **search engine** (Google, Bing) finds pages; a **web page** is one document, a **website** is a collection of pages.

### 3.4 Emerging technologies

- **Artificial Intelligence (AI):** machines performing tasks needing human-like intelligence — learning, reasoning, decision-making. Examples: ChatGPT, voice assistants, recommendation systems, self-driving cars. Subfields: machine learning, deep learning, NLP.
- **Internet of Things (IoT):** everyday objects connected to the internet, collecting and exchanging data — smart watches, home automation, fitness bands, smart agriculture sensors.
- **Cloud computing:** on-demand computing resources (storage, servers, software) over the internet — pay-as-you-go, no local hardware needed. Examples: Google Drive, AWS, Microsoft Azure. Models: **IaaS** (infrastructure), **PaaS** (platform), **SaaS** (software).
- **Cybersecurity basics:** protecting systems/data from attacks. Threats: **virus, worm, trojan, phishing** (fake emails stealing credentials), **ransomware**, hacking. Safety: strong passwords, antivirus, don't click unknown links, keep software updated, backup data.

### Unit 3 — likely exam questions

**Q1. Explain the uses of MS Word, Excel and PowerPoint.**
Model answer: Word — creating/formatting documents, tables, mail merge (.docx). Excel — spreadsheets for data entry, formulas/functions, charts, analysis (.xlsx). PowerPoint — slide presentations with themes, animations, transitions (.pptx).

**Q2. What is a computer network? Differentiate between LAN, MAN and WAN.**
Model answer: A network connects devices to share resources. LAN covers a building/campus (fast, private); MAN covers a city; WAN covers countries/the world — the internet is the biggest WAN. Table from §3.2.

**Q3. Explain network topologies with diagrams.**
Model answer: Bus (single backbone cable), star (all nodes to central hub — most common, easy fault detection), ring (circular, each node to two neighbours), mesh (every node connected to every other — most reliable, costly). Sketch each.

**Q4. Write short notes on: IP address, URL, ISP, TCP/IP.**
Model answer: IP address — unique numeric device address (192.168.1.1); URL — web address of a resource; ISP — company providing internet access; TCP/IP — the protocol suite/rules that make the internet work.

**Q5. Explain email components and the protocols SMTP, POP3, IMAP.**
Model answer: Address format username@domain.com; fields To/Cc/Bcc/Subject/body/attachments. SMTP sends mail; POP3 downloads and usually deletes from server; IMAP keeps mail synced on the server across devices.

**Q6. Write short notes on any two: AI, IoT, cloud computing.**
Model answer: AI — machines mimicking human intelligence (learning, reasoning); examples: assistants, recommendations, self-driving cars. IoT — physical objects connected to the internet sensing/exchanging data; examples: smartwatch, home automation. Cloud — on-demand resources over the internet (Drive, AWS); IaaS/PaaS/SaaS.

**Q7. What is cybersecurity? Explain any four common threats and safety measures.**
Model answer: Protecting systems/data from digital attacks. Threats: virus, phishing (fake mails stealing passwords), ransomware (locks data for money), trojans. Safety: strong unique passwords, antivirus, updated software, avoid suspicious links/attachments, regular backups.

---

## Quick-Revision Checklist (All 3 Units)

**Unit 1 — Computer Fundamentals**
- [ ] IPO cycle, GIGO meaning
- [ ] 6 characteristics: speed, accuracy, diligence, versatility, storage, no IQ/feelings
- [ ] 5 generations + technology + one example each
- [ ] Analog / digital / hybrid; micro, mini, mainframe, supercomputer
- [ ] Block diagram: Input → CPU (ALU + CU) → Output, Memory
- [ ] ALU vs CU roles (CU controls, does NOT process)
- [ ] Number bases: binary 2, octal 8, decimal 10, hex 16
- [ ] Conversions: binary↔decimal, decimal→binary/octal/hex (repeated division), binary→octal/hex (grouping), octal/hex→binary (expansion)
- [ ] BCD (4-bit per digit), ASCII (7/8-bit, A=65), Unicode (universal)
- [ ] Truth tables: AND, OR, NOT; De Morgan's laws

**Unit 2 — Software, OS & Memory**
- [ ] System vs application vs utility software + examples
- [ ] Machine vs assembly vs high-level language
- [ ] Assembler, compiler (whole program), interpreter (line by line) + comparison table
- [ ] OS definition (user–hardware interface) + 6 functions
- [ ] OS types: batch, time-sharing, real-time, distributed, network, mobile
- [ ] Primary (RAM, ROM, cache) vs secondary (HDD, SSD, pen drive) + comparison table
- [ ] Memory hierarchy order: registers → cache → RAM → SSD/HDD → optical/USB → tape
- [ ] Input vs output devices; impact vs non-impact printers

**Unit 3 — Office Tools, Internet & Emerging Tech**
- [ ] Word/Excel/PowerPoint uses + file extensions (.docx, .xlsx, .pptx)
- [ ] Cell, workbook, formula starts with `=`
- [ ] LAN / MAN / WAN ranges; internet = largest WAN
- [ ] Topologies: bus, star, ring, mesh (+ tree)
- [ ] TCP/IP, IP address, URL, ISP, modem/router
- [ ] Email format + To/Cc/Bcc; SMTP (send), POP3/IMAP (receive)
- [ ] Browser vs search engine; web page vs website
- [ ] AI, IoT, cloud (IaaS/PaaS/SaaS) — one definition + two examples each
- [ ] Cybersecurity threats: virus, worm, trojan, phishing, ransomware + safety measures
