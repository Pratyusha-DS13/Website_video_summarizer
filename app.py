import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from pytubefix import YouTube
from langchain.docstore.document import Document
from langchain_community.document_loaders import UnstructuredURLLoader

# --------------------------
# Streamlit APP
# --------------------------
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

with st.sidebar:
    groq_api_key = st.text_input("groq_api", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

# Prompt Template
prompt_template = """
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])


if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YT video URL or website URL")
    else:
        try:
            with st.spinner("Waiting..."):
                # Initialize LLM
                llm = ChatGroq(model="meta-llama/Llama-4-Maverick-17B-128E-Instruct", groq_api_key=groq_api_key)

                # Load content
                if "youtube.com" in generic_url:
                    yt = YouTube(generic_url)
                    transcript = yt.captions.get("a.gu")  # ✅ new way
                    if transcript:
                        text = transcript.generate_srt_captions()
                    else:
                        text = f"Transcript not available for video: {yt.title}"
                    docs = [Document(page_content=text, metadata={"title": yt.title})]
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False
                    )
                    docs = loader.load()

                # Summarize (use invoke instead of run)
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.invoke(docs)

                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")
