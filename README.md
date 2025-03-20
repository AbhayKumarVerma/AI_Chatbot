# 🚀 Setting Up Your Environment with Pipenv

## 📌 Prerequisite: Install Pipenv
Before setting up the environment, ensure **Pipenv** is installed on your system. Follow the official installation guide:  
🔗 [Install Pipenv Documentation](https://pipenv.pypa.io/en/latest/installation.html)

---

## 🛠 Steps to Set Up the Environment

### 🔹 Install Required Packages
To install all necessary dependencies, run the following commands in your terminal (assuming Pipenv is already installed):

```bash
pipenv install langchain langchain_community langchain_huggingface faiss-cpu pypdf
pipenv install huggingface_hub
pipenv install streamlit
```

---

## 📦 Environment Dependencies
Below are the key libraries required for setting up the environment:

### 🔑 Key Libraries
- **LangChain** (`langchain`) - A framework for developing applications powered by large language models (LLMs).
- **LangChain-HuggingFace** (`langchain_huggingface`) - Integration of LangChain with Hugging Face models.
- **FAISS** (`faiss-cpu`) - A high-performance vector similarity search library.
- **PyPDF** (`pypdf`) - A lightweight PDF parsing library.
- **Streamlit** (`streamlit`) - A Python framework for building interactive UI applications.

---

## ⚡ Activate the Virtual Environment
To enter the **Pipenv shell** and work in an isolated environment, use:

```bash
pipenv shell
```

Once activated, all dependencies will be available within this environment.

---

## 🚀 Running Your Application
After setting up the environment and ensuring all dependencies are installed, run the **Streamlit application** with:

```bash
streamlit run app.py
```

> **💡 Note:** Ensure that all dependencies are installed before running the application to avoid errors. If any dependency is missing, reinstall it using `pipenv install`.

---

🎯 Now you're all set! Happy coding! 🚀

