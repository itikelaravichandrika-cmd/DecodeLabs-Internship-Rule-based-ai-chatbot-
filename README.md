# 🤖 Rule-Based AI Chatbot

## Project 1 - Artificial Intelligence

A simple **Rule-Based AI Chatbot** developed using Python.

This chatbot uses predefined rules and `if-else` conditions to decide how to respond to user inputs.

---

## 🎯 Project Goal

The goal of this project is to create a simple rule-based chatbot that can:

* Handle greetings
* Respond to predefined user inputs
* Use `if-else` logic for decision-making
* Continue interacting with the user
* Handle exit commands
* Run in a continuous loop

---

## 🧠 What is Rule-Based AI?

Rule-Based AI is a simple approach where the system follows predefined rules to make decisions.

The chatbot checks the user's input and selects a response based on matching conditions.

For example:

```text
User: Hello
       ↓
Check predefined rules
       ↓
if input == "hello"
       ↓
Bot: Hello! How can I help you today?
```

The chatbot does not use machine learning or a trained AI model.

It follows explicitly programmed rules.

---

## ✨ Features

* Greeting responses
* Basic conversation
* Basic Artificial Intelligence questions
* Basic chatbot questions
* Basic Python questions
* Help response
* Thank-you response
* Exit commands
* Unknown-input response
* Continuous conversation loop

---

## 🛠️ Technology Used

* Python
* If-Else Statements
* Functions
* While Loop
* String Processing

---

## 📁 Project Structure

```text
Rule-Based-AI-Chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

---

## 💻 Requirements

You need:

* Python 3
* VS Code or another Python editor
* Terminal / Command Prompt

No external Python libraries are required.

---

## ▶️ How to Run

### Step 1: Open the project

Open the `Rule-Based-AI-Chatbot` folder in VS Code.

### Step 2: Open the terminal

In VS Code, select:

```text
Terminal → New Terminal
```

### Step 3: Run the program

Type only:

```bash
python chatbot.py
```

Then press **Enter**.

### Important

If your terminal already shows something like:

```text
PS C:\Users\YourName\Rule-Based-AI-Chatbot>
```

do **not** type that part again.

Type only:

```bash
python chatbot.py
```

---

## 💬 Example Conversation

```text
=======================================================
              RULE-BASED AI CHATBOT
=======================================================

Hello! I am RuleBot.
You can ask me about AI, chatbots, Python, or basic questions.
Type 'bye', 'exit', or 'quit' to end the conversation.

You: Hello

RuleBot: Hello! How can I help you today?

You: What is AI?

RuleBot: AI stands for Artificial Intelligence. It is the
ability of machines to perform tasks that normally require
human intelligence.

You: What is Python?

RuleBot: Python is a popular programming language known
for its simple syntax and readability.

You: Bye

RuleBot: Goodbye! Thank you for chatting with me.

-------------------------------------------------------
Chatbot session ended.
=======================================================
```

---

## 🔄 How the Continuous Loop Works

The chatbot uses a `while` loop to continuously receive user input.

```text
Start
  ↓
Display chatbot message
  ↓
Get user input
  ↓
Check predefined rules
  ↓
Generate response
  ↓
Display response
  ↓
Is input an exit command?
  ↓
No ─────────→ Continue conversation
  │
 Yes
  ↓
End chatbot
```

---

## 🚪 Exit Commands

The chatbot can be stopped using:

```text
bye
goodbye
exit
quit
```

For example:

```text
You: exit

RuleBot: Goodbye! Thank you for chatting with me.

Chatbot session ended.
```

---

## ❓ Unknown Inputs

If the chatbot does not find a matching predefined rule, it gives a default response:

```text
You: What is the weather today?

RuleBot: Sorry, I don't understand that question.
Please try another question.
```

This happens because the chatbot only responds to the rules that have been programmed.

---

## 🧩 Main Concepts Used

### 1. Functions

The `get_response()` function determines the chatbot's response.

### 2. If-Else Statements

The chatbot uses `if`, `elif`, and `else` conditions to make decisions.

### 3. String Processing

The input is converted to lowercase and extra spaces are removed.

### 4. While Loop

The `while` loop keeps the chatbot running continuously.

### 5. Decision Making

The chatbot compares the user's input with predefined rules and selects an appropriate response.

---

## 📚 Learning Outcomes

This project demonstrates:

* Control flow
* Decision-making logic
* If-else conditions
* Functions
* Loops
* String handling
* Basic AI concepts
* Rule-based chatbot development

---

## 🚀 Future Improvements

The chatbot can be expanded in the future by adding:

* More predefined rules
* More vocabulary
* Nested conditions
* More conversation responses
* Different chatbot personalities

These improvements can make the chatbot more interactive while still using the rule-based approach.

---

## 👩‍💻 Author

**Ravi Chandrika**

B.Tech - Computer Science and Engineering
Specialization: Artificial Intelligence and Machine Learning

---

## 📌 Project Information

**Project:** Rule-Based AI Chatbot

**Project Type:** Artificial Intelligence

**Programming Language:** Python