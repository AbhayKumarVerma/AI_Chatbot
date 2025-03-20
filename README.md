# README: Setting Up Your Environment with Pipenv

## \( \mathbb{Prerequisite}: \) Install Pipenv
Follow the official Pipenv installation guide to set up Pipenv on your system:  
[Install Pipenv Documentation](https://pipenv.pypa.io/en/latest/installation.html)

---

## \( \mathbb{Steps} \) to Set Up the Environment

### \( \star \) Install Required Packages
To install the required dependencies, run the following commands in your terminal (assuming Pipenv is already installed):

```bash
pipenv install langchain langchain_community langchain_huggingface faiss-cpu pypdf
pipenv install huggingface_hub
pipenv install streamlit
```

### \( \mathbb{Environment} \) Dependencies
The following dependencies are required for setting up the environment:

\[ \mathcal{Key \ Libraries} \]
- \( \mathbf{LangChain} \) \( (\texttt{langchain}) \) - A framework for developing applications powered by large language models (LLMs).
- \( \mathbf{LangChain-HuggingFace} \) \( (\texttt{langchain\_huggingface}) \) - Integration of LangChain with HuggingFace models.
- \( \mathbf{FAISS} \) \( (\texttt{faiss-cpu}) \) - A vector similarity search library optimized for performance.
- \( \mathbf{PyPDF} \) \( (\texttt{pypdf}) \) - A lightweight PDF parsing library for handling document input.
- \( \mathbf{Streamlit} \) \( (\texttt{streamlit}) \) - A Python framework for creating interactive UI applications effortlessly.

### \( \vartriangleright \) Activate the Virtual Environment
To enter the Pipenv shell and work in an isolated environment, use:

```bash
pipenv shell
```

Once activated, all dependencies will be available within this environment.

### \( \mathbb{Running} \) Your Application
After setting up the environment and ensuring all dependencies are installed, run the Streamlit application with:

```bash
streamlit run app.py
```

\( \mathbb{Note:} \) Ensure that all dependencies are installed before running the application to avoid errors. If any dependency is missing, reinstall it using \( \texttt{pipenv install} \).

