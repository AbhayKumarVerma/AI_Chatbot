import os
import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

DB_FAISS_PATH = "vectorstore/db_faiss"

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

def load_llm(huggingface_repo_id, HF_TOKEN):
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repo_id,
        temperature=0.5,
        model_kwargs={"token": HF_TOKEN, "max_length": "512"}
    )
    return llm

def main():
    
    st.set_page_config(
        page_title="AI Chatbot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

   
    st.markdown("""
    <style>
    :root {
        --primary: #6366f1;
        --secondary: #4f46e5;
        --accent: #818cf8;
        --background: #0f172a;
    }
    
    body {
        background-color: var(--background);
        color: white;
    }
    
    .stChatFloatingInputContainer {
        bottom: 20px;
        padding: 0 2rem;
    }
    
    .stChatMessage {
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        max-width: 80%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        animation: slideIn 0.3s ease-out;
    }
    
    .stChatMessage.user {
        background: linear-gradient(145deg, var(--primary), var(--secondary));
        margin-left: auto;
        border-bottom-right-radius: 0;
    }
    
    .stChatMessage.assistant {
        background: linear-gradient(145deg, #1e293b, #334155);
        margin-right: auto;
        border-bottom-left-radius: 0;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .stSidebar {
        background: linear-gradient(195deg, #0f172a, #1e293b);
        border-right: 1px solid #1e293b;
    }
    
    .source-docs {
        background: #1e293b55;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        border-left: 4px solid var(--accent);
    }
    </style>
    """, unsafe_allow_html=True)

   
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>🔮 AI Assistant</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <div style='font-size: 0.9rem; color: #94a3b8;'>
                Powered by Mistral-7B & FAISS
            </div>
            <hr style='border-color: #1e293b; margin: 1.5rem 0;'>
        </div>
        """, unsafe_allow_html=True)
        st.info("💡 Ask me anything! I can help with information from my knowledge base.")

  
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>🤖 AI Chat Assistant</h1>", unsafe_allow_html=True)

    if 'messages' not in st.session_state:
        st.session_state.messages = [{
            'role': 'assistant',
            'content': "Hello! I'm your AI assistant. How can I help you today? 💬"
        }]

    
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'], unsafe_allow_html=True)


    prompt = st.chat_input("Type your message here...")
    
    if prompt:
       
        with st.chat_message('user'):
            st.markdown(f"<div class='user-message'>{prompt}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        with st.spinner(''):
            CUSTOM_PROMPT_TEMPLATE = """
            Use the pieces of information provided in the context to answer user's question.
            If you don't know the answer, just say that you don't know, don't try to make up an answer. 
            Don't provide anything out of the given context

            Context: {context}
            Question: {question}

            Start the answer directly. No small talk please.
            """
            
            HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
            HF_TOKEN = os.environ.get("HF_TOKEN")

            try: 
                vectorstore = get_vectorstore()
                qa_chain = RetrievalQA.from_chain_type(
                    llm=load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID, HF_TOKEN=HF_TOKEN),
                    chain_type="stuff",
                    retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                    return_source_documents=True,
                    chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
                )

                response = qa_chain.invoke({'query': prompt})
                result = response["result"]
                source_documents = response["source_documents"]

                formatted_response = f"""
                {result}
                
                <div class='source-docs'>
                    <strong>📚 Source References:</strong>
                    {''.join([f'<div style="margin: 0.5rem 0;">• {doc.metadata["source"]}</div>' for doc in source_documents])}
                </div>
                """

                with st.chat_message('assistant'):
                    st.markdown(formatted_response, unsafe_allow_html=True)
                st.session_state.messages.append({'role': 'assistant', 'content': formatted_response})

            except Exception as e:
                st.error(f"🚨 Error: {str(e)}")

if __name__ == "__main__":
    main()