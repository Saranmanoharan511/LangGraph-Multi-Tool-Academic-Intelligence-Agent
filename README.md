# 🎓 LangGraph Multi-Tool Academic Intelligence Agent

An AI-powered Academic Intelligence Agent built using LangGraph, Ollama, SQL, RAG, and Python Analytics to assist with student performance analysis, academic policy retrieval, and risk assessment.

The system combines structured student data from the OULAD dataset with unstructured university policy documents to provide intelligent, context-aware responses through a multi-tool agent architecture.

---

## 🚀 Project Overview

This project demonstrates how Agentic AI can be applied in the education domain by combining:

- 📊 SQL-based student analytics
- 📚 Retrieval-Augmented Generation (RAG)
- 🐍 Python-based analytical reasoning
- 🤖 Local LLM inference using Ollama
- 🔄 Multi-tool orchestration with LangGraph

The agent can answer questions about:

- Student performance
- Assessment results
- Student engagement
- Academic regulations
- Attendance policies
- Examination rules
- Student risk assessment
- Educational insights and recommendations

---

## 🏗️ Architecture

```text
                        User Query
                             │
                             ▼
              ┌──────────────────────────┐
              │ LangGraph Agent (Qwen3) │
              └─────────────┬────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
 ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
 │   SQL Tool     │ │   RAG Tool     │ │ Python Tool    │
 │ (SQLite/OULAD) │ │ (Student Docs) │ │ (Analytics)    │
 └────────────────┘ └────────────────┘ └────────────────┘
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                    Final Response
```

---

## 🛠️ Tech Stack

### Agent Framework
- LangGraph
- LangChain

### LLM
- Qwen3:8B (Ollama)

### Vector Database
- FAISS

### Embeddings
- nomic-embed-text

### Database
- SQLite

### Dataset
- OULAD (Open University Learning Analytics Dataset)

### Document Processing
- PyPDF
- Recursive Character Text Splitter

### Analytics
- Python REPL Tool

---

## 🔧 Tools Used By The Agent

### 1. SQL Tool

Uses SQLite and the OULAD dataset to answer questions about student data.

Examples:

- Show student information
- Calculate assessment averages
- Retrieve registration details
- Analyze engagement metrics
- Compare module performance

Example Query:

```text
Which student has the highest overall score?
```

---

### 2. Academic RAG Tool

Uses university handbook documents stored in a FAISS vector database.

Examples:

- Attendance requirements
- Examination policies
- Academic misconduct rules
- Student support services
- Progression requirements

Example Query:

```text
What is the minimum attendance requirement?
```

---

### 3. Python Analytics Tool

Performs calculations and analytical reasoning beyond SQL.

Examples:

- Risk scoring
- Performance trend analysis
- Cohort comparison
- Percentile calculations
- Statistical summaries

Example Query:

```text
Compare student 45642 with class average performance.
```

---

## 📚 Dataset

### OULAD (Open University Learning Analytics Dataset)

The project uses the OULAD dataset containing:

| Table | Description |
|---------|-------------|
| studentInfo | Student demographics and outcomes |
| studentAssessment | Assessment scores |
| assessments | Assessment metadata |
| studentRegistration | Registration records |
| courses | Course information |
| studentVle | Student online activity |
| vle | Virtual Learning Environment resources |

---

## 📄 Knowledge Base

The RAG component uses:

- Student Handbook
- Academic Regulations
- Examination Policies
- Attendance Rules

These documents are indexed using:

- RecursiveCharacterTextSplitter
- nomic-embed-text embeddings
- FAISS Vector Store

---

## 💡 Example Queries

### SQL-Based Queries

```text
Give me details of student with student id 45642
```

```text
Which module has the highest failure rate?
```

```text
List the top 10 performing students.
```

---

### RAG-Based Queries

```text
What happens if a student has low attendance?
```

```text
Can students retake failed exams?
```

```text
What is considered academic misconduct?
```

---

### Analytics Queries

```text
Compare student 45642 with class average performance.
```

```text
Classify students into low, medium, and high risk categories.
```

---

### Multi-Tool Queries

```text
Identify at-risk students and explain university support policies.
```

```text
Find failing students and recommend actions based on handbook rules.
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd LangGraph-MultiTool-Academic-Intelligence-Agent
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Install Ollama Models

Pull the LLM:

```bash
ollama pull qwen3:8b
```

Pull embedding model:

```bash
ollama pull nomic-embed-text
```

---

### Start Ollama

```bash
ollama serve
```

---

## ▶️ Running The Project

Open the notebook:

```bash
jupyter notebook
```

Run:

```text
Academic_Intelligence_Agent.ipynb
```

Execute all cells.

---

## 🎯 Key Features

- Multi-tool agent architecture
- Local LLM inference
- SQL reasoning
- Retrieval-Augmented Generation
- Educational analytics
- Risk assessment
- Student engagement analysis
- Academic policy retrieval
- LangGraph workflow orchestration

---

## 📈 Future Improvements

- Student dropout prediction
- Personalized study recommendations
- Visualization dashboard
- Multi-agent architecture
- Real-time university integration
- Advanced educational analytics
- Streamlit deployment
- Evaluation framework

---

## 🧠 Learning Outcomes

This project demonstrates:

- Agentic AI Systems
- LangGraph Workflows
- Tool Calling
- RAG Pipelines
- Vector Databases
- Local LLM Deployment
- Educational Data Analytics
- SQL Agent Design
- Multi-Tool Reasoning

---

## 👨‍💻 Author

Saran Manoharan

Built as a hands-on Agentic AI and Educational Analytics project using LangGraph, Ollama, SQL, RAG, and Python analytics.
