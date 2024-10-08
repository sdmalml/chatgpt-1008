import streamlit as st
from langchain_aws.chat_models import ChatBedrock

st.title("ChatGPT-like clone")
EMBEDDING_MODEL_ID = 'amazon.titan-embed-text-v2:0'
CLAUDE_HAIKU_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
CLAUDE_SONNET_ID = 'anthropic.claude-3-5-sonnet-20240620-v1:0'

chat_model = ChatBedrock(model_id=CLAUDE_HAIKU_ID)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = chat_model.stream(prompt)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})