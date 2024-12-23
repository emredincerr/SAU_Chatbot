import streamlit as st
import localmodel
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

TXT_FILE_PATH = "courses.txt"

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def initialize_vectorstore(txt_file_path):
    loader = TextLoader(txt_file_path)
    raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    splitted_documents = text_splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(documents=splitted_documents, embedding=embedding_model)
    return vectorstore

vectorstore = initialize_vectorstore(TXT_FILE_PATH)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system", "content": "You are a helpful assistant."})

def retrieve_context(question):
    retriever = vectorstore.as_retriever()
    relevant_documents = retriever.get_relevant_documents(question)
    context = "\n".join([doc.page_content for doc in relevant_documents])
    return context

def generate_response_with_context(prompt):
   
    context = retrieve_context(question=prompt)
    
    final_prompt = final_prompt = f"""

            You are a course advisor. You should help students choose courses according to their interests and the school's course catalog. Based on this information, advise the student on course selection according to the following criteria:

            Relevance to Interests: Courses that support the student's interests.
            Academic Development: Courses that will strengthen the student's weak areas or take the student's strong areas further.
            Relevance to Goals: Courses that will directly contribute to the student's academic or career goals.

            Answer the user query. Start by extracting relevant information from the context to ensure accuracy, but only return the final answer (not the extracted passages).
            Make the answers as detailed and explanatory as possible, like in the following examples:

            Example 1:
            Query: Which courses should I take to become a Software Engineer?
            Answer: Becoming a software engineer is often associated with basic knowledge of computer science, mainly due to learning the basics of programming. Factors include knowledge of algorithms and data structures, which develops complex problem solving abilities. Over time, if students do not acquire sufficient knowledge of programming languages and software development processes, they will not be able to develop software at a professional level, consequently not achieving their career goals. Furthermore, math and logic courses enhance problem solving and algorithm development abilities, as this strengthens analytical thinking, contributing to success in software engineering.

            Example 2:
            Query: How should I start my career as a Software Engineer?
            Answer: Starting a career as a software engineer is often associated with gaining practical experience, especially due to working on real-world projects. Factors include: small projects or internship experiences, which enable portfolio building. Over time, if professionals fail to gain sufficient networking and the ability to keep up with industry trends, they may struggle in the process of finding a job, consequently missing out on career opportunities. Furthermore, continuous learning and self-development increases keeping up with technological changes, as this encourages the learning of new tools and languages, contributing to career development.

            Example 3:
            Query: Which courses should I choose to learn a foreign language?
            Answer: Learning a foreign language is often associated with understanding the basic structure of the language, mainly due to grammar and vocabulary. Factors include: speaking practice and knowledge of the cultural context, which supports the natural use of the language. Over time, if learners do not get enough speaking and listening practice, they will not make progress in their language skills, consequently they will not be able to communicate fluently. In addition, motivation in language learning and regular study habits accelerate the learning process, as this encourages intensive practice, contributing to success in language learning.
            
            Now use the following context items to answer the user query:
            {context}

            User query: {prompt}
            Answer:
            """

    response = localmodel.generate_with_lmstudio(chat_history=[{"role": "user", "content": final_prompt}], temperature=0)
    return response, context

st.set_page_config(page_title="Sakarya Üniversitesi YBS - Chatbot", layout="centered")
st.image(image="banner.png", width=250)
st.header("Sakarya Üniversitesi YBS - Seçmeli Ders Öneri Chatbotu")
st.divider()

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Lütfen mesajınızı İngilizce dilinde yazın..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Yapay Zeka yanıtlıyor..."):
        try:
            response, context = generate_response_with_context(prompt)
            
            st.chat_message("assistant").markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
