# 🤖 AI Interview Coach

An AI-powered Interview Preparation Platform built using **LangChain**, **Ollama**, and **Streamlit**.

The application analyzes a candidate's **Resume** against a **Job Description**, conducts an **interactive AI mock interview**, and finally generates a **detailed performance report** with personalized feedback.

---

# 🚀 Features

## 📄 Resume Analysis

- Compare Resume with Job Description
- ATS-style Match Score
- Resume Summary
- Job Description Summary
- Matching Skills
- Missing Skills
- Resume Improvement Suggestions
- Overall Resume Feedback

---

## 💬 AI Mock Interview

- Generates interview questions based on Resume Analysis
- Focuses more on missing skills and weak areas
- Questions increase in difficulty gradually
- Maintains interview context throughout the session
- Streams questions in real-time for a ChatGPT-like experience

---

## 📊 Interview Performance Report

After the interview, the application generates a complete report including:

- Overall Interview Score
- Overall Feedback
- Candidate Strengths
- Areas for Improvement
- Recommended Learning Topics
- Interview Tips
- Question-wise Evaluation
- Ideal Answers for every question

---

# 🛠️ Tech Stack

### AI

- LangChain
- Ollama
- Qwen2.5:3B

### Backend

- Python

### UI

- Streamlit

### LLM Concepts

- Prompt Engineering
- Prompt Templates
- Chains
- JSON Output Parser
- String Output Parser
- Streaming Responses
- Session State Memory

---

# 🏗️ Project Architecture

```
                 Resume
                    │
                    │
          Job Description
                    │
                    ▼
          Resume Analysis Chain
                    │
                    ▼
          Structured JSON Output
                    │
                    ▼
           Start Interview
                    │
                    ▼
        Interview Question Chain
                    │
        (Streaming Questions)
                    │
                    ▼
          Interview Conversation
                    │
                    ▼
         Interview Feedback Chain
                    │
                    ▼
         Final Interview Report
```

---

# ⚙️ Workflow

## Step 1

Paste the Resume.

## Step 2

Paste the Job Description.

## Step 3

The Resume Analysis Chain evaluates:

- Resume Summary
- JD Summary
- Match Score
- Matching Skills
- Missing Skills
- Resume Improvements

## Step 4

Start the AI Mock Interview.

The Interview Chain:

- Reads Resume Analysis
- Generates one question at a time
- Uses previous conversation to maintain context
- Streams responses

## Step 5

After completing the interview, the Feedback Chain evaluates:

- Overall Score
- Strengths
- Weaknesses
- Learning Roadmap
- Interview Tips
- Question-wise Feedback
- Ideal Answers

---

# 🧠 LangChain Components Used

## PromptTemplate

Used for creating reusable prompts.

### Resume Analysis Prompt

Analyzes Resume and Job Description.

### Interview Prompt

Generates interview questions.

### Feedback Prompt

Evaluates interview performance.

---

## Chains

### Resume Analysis Chain

```
Prompt
    ↓
LLM
    ↓
JSON Parser
```

---

### Interview Chain

```
Prompt
    ↓
LLM
    ↓
String Parser
    ↓
Streaming
```

---

### Feedback Chain

```
Prompt
    ↓
LLM
    ↓
JSON Parser
```

---

# 📂 Project Structure

```
AI-Interview-Coach/

│── app.py
│── chains.py
│── prompts.py
│── models.py
│── requirements.txt
│── README.md
```

---

# 📸 Screenshots

> Add screenshots of:

- Resume Analysis
- AI Interview
- Final Interview Report

---

# 💡 Future Improvements

- Chat History UI
- Authentication
- Resume Upload (PDF/DOCX)
- Voice-based Interview
- Speech-to-Text
- Text-to-Speech
- Export Interview Report as PDF
- Save Interview History
- Multiple LLM Support
- Cloud Deployment
- RAG-powered Company Specific Interviews
- AI Career Roadmap Generation

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience with:

- LangChain
- Ollama
- Prompt Engineering
- LLM Workflows
- JSON Parsing
- Streaming Responses
- Session State Management
- Building Multi-step AI Applications
- Designing AI Pipelines

---

# ▶️ Getting Started

## Clone the repository

```bash
git clone https://github.com/your-username/AI-Interview-Coach.git
```

```bash
cd AI-Interview-Coach
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama

Pull the model:

```bash
ollama pull qwen2.5:3b
```

Run Ollama:

```bash
ollama serve
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 🌟 Demo

1. Paste Resume
2. Paste Job Description
3. Analyze Resume
4. Start Mock Interview
5. Answer Questions
6. Generate Interview Report

---

# 🤝 Contributions

Contributions, suggestions, and feedback are always welcome.

Feel free to fork the repository, raise issues, or submit pull requests.

---

# ⭐ If you found this project useful, consider giving it a star!