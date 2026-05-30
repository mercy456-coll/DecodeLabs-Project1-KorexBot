# ============================================
# KorexBot - Rule-Based AI Chatbot
# Built by: Mercy, DecodeLabs AI Intern
# Project 1: Industrial Training Kit | Batch 2026
# ============================================

# --- KNOWLEDGE BASE (Dictionary) ---
# Each key is what the user might type.
# Each value is what KorexBot will reply.

responses = {

    # Greetings
    "hello": "Hey there! I'm KorexBot, your AI assistant. What's on your mind?",
    "hi": "Hi! Great to see you. Ask me anything about AI, Python, or DecodeLabs!",
    "hey": "Hey! KorexBot is online and ready. How can I help?",
    "good morning": "Good morning! Let's learn something great today.",
    "good evening": "Good evening! I'm here if you need me.",

    # Identity
    "who are you": "I'm KorexBot — a rule-based AI chatbot built during the DecodeLabs internship. No hallucinations, just logic.",
    "what is your name": "My name is KorexBot! Built with pure Python logic.",
    "who made you": "I was built by Mercy, a DecodeLabs AI intern as part of Project 1 — Batch 2026.",
    "are you human": "Nope! I'm 100% rule-based logic. No neural network here — just clean Python.",

    # AI Knowledge
    "what is ai": "AI stands for Artificial Intelligence — teaching machines to simulate human thinking through data and logic.",
    "what's ai": "AI stands for Artificial Intelligence. It is the science of teaching machines to think, reason, and make decisions the way humans do — turning raw data into smart actions.",
    "what is machine learning": "Machine Learning is a branch of AI where systems learn from data patterns without being explicitly programmed.",
    "what is deep learning": "Deep Learning uses neural networks with many layers to recognize complex patterns like images and speech.",
    "what is a neural network": "A neural network is a system of algorithms modeled after the human brain that processes data in layers.",
    "what is nlp": "NLP stands for Natural Language Processing — it helps computers understand and respond to human language.",
    "what is a large language model": "A Large Language Model (LLM) is a deep learning model trained on massive text data to generate human-like responses.",
    "difference between ai and ml": "AI is the broad concept of machines being smart. ML is a subset of AI — it's the method used to achieve that smartness.",
    "what is a rule based system": "A rule-based system responds using hardcoded if-then logic. It is 100% predictable, traceable, and has zero hallucination risk.",  "what are ai guardrails": "AI guardrails are rule-based filters placed around LLMs to block unsafe, harmful, or off-topic outputs.",

    # Python Knowledge
    "what is python": "Python is a beginner-friendly programming language widely used in AI, data science, and web development.",
    "what is a dictionary in python": "A Python dictionary stores data as key-value pairs. In KorexBot, it stores intents and their responses!",
    "what is a while loop": "A while loop repeats a block of code as long as a condition is True — like how I keep listening for your input!",
    "what is a function": "A function is a reusable block of code that performs a specific task when called.",
    "what does lower do": "The .lower() method converts text to lowercase — so 'Hello' and 'hello' are treated the same.",
    "what does strip do": "The .strip() method removes extra spaces from both ends of your input so I don't misread you.",

    # DecodeLabs
    "what is decodelabs": "DecodeLabs is a tech training platform that gives interns real industry-level projects to build their portfolios.",
    "what is project 1": "Project 1 is the Rule-Based AI Chatbot — the foundation project every DecodeLabs AI intern must complete first.",
    "how many projects are there": "There are 4 projects in total — one per week. Complete them all to earn your certificate and letter of recommendation!",
    "what do i get at the end": "Interns who complete all projects earn a certificate AND a letter of recommendation from DecodeLabs!",

    # Help & General
    "what can you do": "I can answer questions about AI, machine learning, Python, and DecodeLabs. Try asking me anything!",
    "help": "Sure! Ask me about: AI concepts, Python basics, DecodeLabs projects, or just say hello!",
    "tell me something interesting": "Fun fact: The first AI chatbot ever built was ELIZA in 1966 — and it also used rule-based logic, just like me!",
    "thank you": "You're welcome! Keep building and keep learning.",
    "thanks": "Anytime! That's what I'm here for.",

    # Exit
    "bye": "Goodbye! Keep pushing forward — you're building something great.",
    "goodbye": "See you next time! KorexBot signing off.",
    "farewell": "Farewell! It was great chatting with you. Keep building!",
    "ciao": "Ciao! Come back anytime.KorexBot will be here!"
}

# --- WELCOME BANNER ---

print("=" * 50)
print("          Welcome to KorexBot")
print("   Rule-Based AI Chatbot | DecodeLabs 2026")
print("=" * 50)
print()
print("  Here is what you can do:")
print("  - Ask me about AI, Python, or DecodeLabs")
print("  - Type 'help'  -> see what I know")
print("  - Type 'exit'  -> end the conversation")
print("  - Type 'quit'  -> also ends the conversation")
print()
print("=" * 50)
print()

# --- MAIN CHATBOT LOOP ---

while True:

    # PHASE 1: Get and sanitize input
    user_input = input("You: ").lower().strip()
    

    # PHASE 2: Exit strategy
    if user_input in ["exit", "quit"]:
        print("KorexBot: Goodbye! Session ended. Keep building!")
        break

    # PHASE 3: Skip empty inputs
    if user_input == "":
        print("KorexBot: Please type something — I'm listening!")
        continue

    # PHASE 4: Dictionary lookup with fallback
    reply = responses.get(user_input, "I don't understand that yet. Try rephrasing or type 'help' to see what I know!")

    # PHASE 5: Display response
    print(f"KorexBot: {reply}\n")