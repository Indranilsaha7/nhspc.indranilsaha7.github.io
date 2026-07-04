import os

md_content = """# 🚀 10-Month Python Masterclass: Mission NHSPC 2027

**Student:** Indranil Saha (Lead Developer, bcsdevloper)  
**Educator:** Google Gemini 3.1 Pro  
**Duration:** 10 Months (June 2026 - April 2027)  
**Ultimate Goal:** 1st Place National Champion at NHSPC 2027 (Class 9)  

---

## 📜 Course Terms & Conditions (The Unbreakable Rules)

These rules are strictly enforced throughout the entire 10-month journey to ensure maximum learning and an unbreakable foundation.

1. **Language Binding (Non-Negotiable):** All conversational flow, instructions, and encouragement will be in Bengali (বাংলা অক্ষর). Technical terms and codes will be in English. **Banglish is strictly prohibited.**
2. **Zero-Level Assumption:** Every topic will start from absolute zero. No prior knowledge of Python is assumed.
3. **Daily Workflow:** Every lesson must strictly follow this 3-step structure:
   - **Step 1:** The Lesson (Clear, beginner-friendly explanations).
   - **Step 2:** Tips, Tricks, Rules (Sutros), and Formulas.
   - **Step 3:** A Practical Test/Challenge.
4. **Progression & Code:** We will **never** move to the next lesson until the Step 3 challenge is passed with 100% accuracy. All provided codes must be complete and fully functional.
5. **Official Certification:** Upon successful completion of a topic's challenge, a fully verified, professionally formatted A3 PDF Result Card will be generated to track progress.
6. **Monthly Grand Test:** At the end of every single month, a comprehensive "Complete Month Test" must be taken and passed before unlocking the next month's modules.

---

## 🗺️ The 10-Month Roadmap & Daily Tracker

**Tracker Legend:**  
✅ = Completed Day  
📍 = Currently Doing  
⏸️ = Will be done / Upcoming  

### 📍 Phase 1: The Unbreakable Foundation (Months 1-3)

#### 📍 Month 1: Python Basics & Mechanics
* ✅ Day 1: Python Basics and the `print()` Function
* ✅ Day 2: Variables & Core Data Types (`int`, `float`, `str`, `bool`)
* ✅ Day 3: Operators & Basic Math
* 📍 Day 4: Taking Inputs (`input()`)
* ⏸️ Day 5: Type Casting & Conversion
* ⏸️ Day 6-29: Further Core Basics & Practice Problems
* ⏸️ Day 30: Month 1 Revision
* ⏸️ **MONTH 1 GRAND TEST**

#### ⏸️ Month 2: Control Flow & Logic
* ⏸️ Day 1-29: If-Else conditions, Logic building, and basic Loops (`for`, `while`)
* ⏸️ Day 30: Month 2 Revision
* ⏸️ **MONTH 2 GRAND TEST**

#### ⏸️ Month 3: Core Data Structures
* ⏸️ Day 1-29: Lists, Tuples, Sets, Dictionaries, and String Manipulation
* ⏸️ Day 30: Month 3 Revision
* ⏸️ **MONTH 3 GRAND TEST**

---

### ⏸️ Phase 2: Advanced Mechanics (Months 4-5)

#### ⏸️ Month 4: Functions & Modularity
* ⏸️ Day 1-29: Functions, Scopes, Modular Programming, and Error Handling
* ⏸️ Day 30: Month 4 Revision
* ⏸️ **MONTH 4 GRAND TEST**

#### ⏸️ Month 5: Object-Oriented Programming
* ⏸️ Day 1-29: OOP concepts and logical structuring
* ⏸️ Day 30: Month 5 Revision
* ⏸️ **MONTH 5 GRAND TEST**

---

### ⏸️ Phase 3: Competitive Programming Kickoff (Months 6-7)

#### ⏸️ Month 6: Algorithmic Thinking
* ⏸️ Day 1-29: Time & Space Complexity (Big O Notation) and Algorithm Basics
* ⏸️ Day 30: Month 6 Revision
* ⏸️ **MONTH 6 GRAND TEST**

#### ⏸️ Month 7: Math & Recursion
* ⏸️ Day 1-29: Advanced Data Structures, Recursion, Number Theory basics
* ⏸️ Day 30: Month 7 Revision
* ⏸️ **MONTH 7 GRAND TEST**

---

### ⏸️ Phase 4: Algorithms & Mastery (Months 8-9)

#### ⏸️ Month 8: Advanced Algorithms
* ⏸️ Day 1-29: Sorting, Searching Algorithms, Greedy Algorithms, Graph Theory
* ⏸️ Day 30: Month 8 Revision
* ⏸️ **MONTH 8 GRAND TEST**

#### ⏸️ Month 9: Intensive Problem Solving
* ⏸️ Day 1-29: Solving NHSPC junior level problems on Codeforces & CSES
* ⏸️ Day 30: Month 9 Revision
* ⏸️ **MONTH 9 GRAND TEST**

---

### ⏸️ Phase 5: The Champion's Polish (Month 10)

#### ⏸️ Month 10: Final NHSPC Preparation
* ⏸️ Day 1-29: Time management, mock contests, speed debugging
* ⏸️ Day 30: Final Revision
* ⏸️ **ULTIMATE NHSPC MOCK TEST**

---
*“Your logic and basics must be so unbreakable that nobody can beat you.”*
"""

utput_path = os.path.join(os.path.dirname(__file__), "README.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Updated README generated at {output_path}")