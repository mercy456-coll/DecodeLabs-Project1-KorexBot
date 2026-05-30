# 🤖 KorexBot — Rule-Based AI Chatbot
### DecodeLabs AI Engineering Internship | Project 1 | Batch 2026

---

## 📌 Project Overview

Before neural networks. Before LLMs. Before "AI" became a buzzword — there were **rule-based systems.**

KorexBot is a rule-based AI chatbot built entirely in Python using pure programmatic logic. No APIs. No machine learning. No external frameworks. Just structured decision-making that simulates intelligent conversation through **dictionary-based intent matching**, **input sanitization**, and a **continuous loop architecture.**

This project demonstrates that the foundation of every intelligent system — no matter how advanced — is solid, well-structured logic.

---

## 🎯 Project Goal

Build a simple rule-based chatbot that:
- Responds intelligently to predefined user inputs
- Handles greetings, farewells, and topic-based queries
- Runs in a continuous loop until the user exits
- Sanitizes all user input for consistent matching
- Returns a graceful fallback for unknown inputs

---

## ⚙️ Key Features

| Feature | Description |
|---|---|
| 🧠 Knowledge Base | Dictionary with 35+ intents across multiple topics |
| 🔄 Continuous Loop | Runs indefinitely using a `while True` architecture |
| 🧹 Input Sanitization | Converts input to lowercase and strips whitespace |
| 💬 Fallback Response | Handles unknown inputs gracefully |
| 🚪 Exit Strategy | Clean session termination via `exit` or `quit` |
| 👋 Welcome Banner | Clear user guide displayed at startup |
| 🛡️ Empty Input Guard | Handles blank inputs without crashing |

---

## 📚 Topics KorexBot Knows About

- 🤖 **Artificial Intelligence** — definitions, concepts, guardrails
- 🧬 **Machine Learning & Deep Learning** — key terminology
- 🐍 **Python Programming** — dictionaries, loops, functions, methods
- 🏢 **DecodeLabs** — internship structure, projects, rewards
- 💬 **General Conversation** — greetings, farewells, fun facts

---

## 🏗️ Architecture

```
User Input
    ↓
Input Sanitization (.lower().strip())
    ↓
Exit Check — is it "exit" or "quit"?
    ↓ NO
Empty Input Check
    ↓
Dictionary Lookup (responses.get())
    ↓
Match Found?  →  YES  →  Return Response
              →  NO   →  Return Fallback
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** None — pure Python only
- **Paradigm:** Rule-Based / Deterministic AI
- **Interface:** Command Line (Terminal)

---

## 🚀 How to Run

**Step 1 — Make sure Python 3 is installed**
```bash
python --version
```

**Step 2 — Clone this repository**
```bash
git clone https://github.com/yourusername/DecodeLabs-Project1-KorexBot.git
```

**Step 3 — Navigate to the folder**
```bash
cd DecodeLabs-Project1-KorexBot
```

**Step 4 — Run KorexBot**
```bash
python korexbot.py
```

---

## 💻 Sample Conversation

```
==================================================
          Welcome to KorexBot
   Rule-Based AI Chatbot | DecodeLabs 2026
==================================================

  Here is what you can do:
  - Ask me about AI, Python, or DecodeLabs
  - Type 'help'  -> see what I know
  - Type 'exit'  -> end the conversation
  - Type 'quit'  -> also ends the conversation

==================================================

You: hello
KorexBot: Hey there! I'm KorexBot, your AI assistant. What's on your mind?

You: what is ai
KorexBot: AI stands for Artificial Intelligence. It is the science of teaching 
machines to think, reason, and make decisions the way humans do.

You: who made you
KorexBot: I was built by Mercy, a DecodeLabs AI intern as part of Project 1 — Batch 2026.

You: exit
KorexBot: Goodbye! Session ended. Keep building!
```

---

## 🧠 Key Concepts Demonstrated

- **Deterministic AI** — 100% predictable, traceable outputs
- **White Box System** — every decision is fully explainable
- **IPO Model** — Input → Process → Output architecture
- **Hash Map Efficiency** — O(1) dictionary lookup vs O(n) if-elif ladder
- **Input Normalization** — sanitization for consistent user experience

---

## 📖 What I Learned

Building KorexBot taught me that intelligence doesn't always require complexity. The most reliable AI systems are built on a foundation of clear, structured logic. Before you can manage the chaos of a probability engine, you must master the precision of a logic engine.

This project is the skeleton that every advanced AI system is built upon.

---

## 👩‍💻 Built By

**Mercy Inameti**
AI Engineering Intern — DecodeLabs Batch 2026
Project 1| Rule-Based AI Chatbot

---

*"An LLM without rules is a hallucination engine. Today, we build the skeleton that holds the intelligence." — DecodeLabs*

