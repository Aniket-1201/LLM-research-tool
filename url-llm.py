import os
import streamlit as st
import time
import pickle
from langchain_community.chat_models import ChatGooglePalm
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


st.title("News Research tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
main_placeholder = st.empty()
api_key = "your api key"

llm = ChatGooglePalm(google_api_key = api_key,temperature=0.5,max_tookens = 500)
vector_file_path = "vector_index-1"
if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
    vectordb = FAISS.from_documents(documents=docs,embedding=embeddings)
    vectordb.save_local(vector_file_path)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file

   # with open(file_path, "wb") as f:
      #  pickle.dump(vectordb, f)

query = main_placeholder.text_input("Question: ")
if query:
   # if os.path.exists(file_path):
      #  with open(file_path, "rb") as f:
            #vectorIndex = pickle.load(f)
            embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
           # vectorstore = FAISS.from_documents(docs, embeddings)
            vectordb = FAISS.load_local(vector_file_path, embeddings,allow_dangerous_deserialization=True)
            retriever = vectordb.as_retriever(score_threshold=0.7)
            prompt_template = """Given the following context and a question, generate an answer based on this context only.
            In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
            If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

            CONTEXT: {context}

            QUESTION: {question}"""

            PROMPT = PromptTemplate(
                template=prompt_template, input_variables=["context", "question"]
            )
            chain_type_kwargs = {"prompt": PROMPT}
            chain = RetrievalQA.from_chain_type(llm=llm,
                                                chain_type="stuff",
                                                retriever=retriever,
                                                input_key="query",
                                                return_source_documents=True,
                                                chain_type_kwargs=chain_type_kwargs)
            result = chain({"query": query})
            # Safely access the answer
            st.header("Answer")
            answer = result.get("result", "No answer found.")
            st.write(answer)
            st.header("Debugging Info")
            st.write(result)
            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)

