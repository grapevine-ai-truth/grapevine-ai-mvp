# 🍇 Grapevine AI – MVP

**Grapevine AI** is a new kind of digital assistant — one that protects you from manipulation, misinformation, and shady communication online.

This MVP (Minimum Viable Product) is the foundation of a larger platform aimed at helping users **verify what they’re seeing**, **analyze the intent behind messages**, and **respond smartly with AI**.

> “In a world where lies move faster than truth, we give people a head start.”

---

## 🚀 Vision

The internet is overwhelmed with scams, manipulative messages, and half-truths — from phishing emails to fake influencers to shady DMs. Grapevine AI is here to flip that script.

Our mission is to build the **"blockchain of credibility"** — a smart, AI-driven system for verifying claims, scoring trustworthiness, and generating safe responses, right inside your inbox or DMs.

This MVP lays the groundwork for:
- 🔍 **Message analysis**
- 🤖 **GPT-powered auto-responses**
- 🧠 **Credibility scoring ("TruthScore")**
- 🚨 **Suspicious link detection**

And eventually, we'll expand toward:
- ✅ Public identity verification
- 🌐 Distributed reputation systems
- 🔗 Blockchain-backed proof-of-trust

---

## 🧪 What This MVP Can Do

| Feature | Description |
|--------|-------------|
| 🧠 GPT Outreach Engine | Takes any incoming message and generates a helpful, safe reply using OpenAI’s GPT-4 |
| 🧪 TruthScore Engine | Assigns a credibility score (0–100) based on sender behavior, language, and links |
| 🔗 Link Scanner | Flags malicious or suspicious URLs in messages |
| 📬 Gmail Integration (coming) | Enables in-inbox scoring and reply suggestions (via Gmail API + OAuth2) |

---

## 🛠️ Tech Stack

- Python 3.10+
- Google Colab
- OpenAI API (GPT-4 / GPT-3.5)
- `dotenv`, `openai`, `re`, `tldextract`

---

## 📁 File Structure

grapevine-ai-mvp/
├── .env # [SECRET] Contains your OpenAI API key
├── requirements.txt # Required packages
├── main.ipynb # Main Google Colab notebook to run MVP
├── outreach_engine.py # GPT-based response generation logic
├── truthscore.py # Message credibility scoring module
├── link_scanner.py # Detects suspicious or malicious URLs
├── utils.py # Helper functions (optional)
└── README.md # You're reading it

---


---

## ▶️ How to Use

1. **Clone the repo** or open the `main.ipynb` notebook in [Google Colab](https://colab.research.google.com).
2. Follow the notebook cells in order.
3. The notebook will:
   - Load your `.env` securely
   - Let you input sample messages or emails
   - Return credibility scores, response suggestions, and link risk checks

> 🚧 **Note:** Gmail integration is in development. This MVP is currently CLI + notebook driven.

---

## 🔐 Environment Setup

1. Create a `.env` file in your root folder (not pushed to GitHub):
    ```
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure your `.env` is included in `.gitignore` to keep it private.

---

## 🛣️ Roadmap

We’re just getting started. Here’s where Grapevine AI is going:

- [x] MVP with GPT outreach, TruthScore, and link scanner
- [ ] Gmail integration with inline TruthScores
- [ ] Realtime dashboard + alerts
- [ ] Public TruthScore API for fact-checking messages
- [ ] Verified Web3/identity system (blockchain layer)
- [ ] Native Chrome Extension or Gmail Add-on
- [ ] Open source community contributions

---

## 🤝 Collaborate or Support

If you believe in this mission, I’d love your help:
- Code contributions (see Issues)
- Design/UX improvements
- Outreach & evangelism
- Ethical AI guidance

📬 Email: **grapevine.ai.truth@gmail.com**  
🔗 GitHub: [@grapevine-ai-truth](https://github.com/grapevine-ai-truth)

---

## 📜 License

This project is in pre-release. License will be finalized post-launch.  
For now, feel free to fork and experiment — all credit welcome.

> *“They say the grapevine spreads rumors. We built Grapevine AI to spread truth.”*

---
