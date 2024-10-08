import streamlit as st
from app_factory import AppFactory
from pdf_handler import upload_and_extract_pdf
from search_handler import search_web  # Tavily 검색 핸들러 추가
from thread_handler import save_thread, load_thread, list_threads
from code_interpreter import execute_code
import getpass
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()  # API 키 입력
os.environ["LANGCHAIN_API_KEY"] = "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"  # API 키 입력
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["TAVILY_API_KEY"] = "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"

def main():
    """메인 함수는 앱을 초기화하고 실행한다."""
    st.title("ChatGPT 클론 코딩 with Tavily")

    # 시스템 프롬프트 입력 추가
    system_prompt = st.text_input("System Prompt를 입력하세요.", "You are a helpful assistant.")

    # PDF 파일 업로드 기능
    uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")
    extracted_text = ""
    if uploaded_file:
        extracted_text = upload_and_extract_pdf(uploaded_file)
        st.text_area("Extracted Text", extracted_text)

    # Tavily 실시간 검색 기능
    query = st.text_input("실시간 검색어를 입력하세요:")
    if query:
        results = search_web(query)
        if results:
            st.write("검색 결과:")
            for result in results:
                st.write(result["title"])
                st.write(result["url"])

    # 대화 쓰레드 관리 기능
    thread_id = st.text_input("대화 쓰레드 ID 입력:")
    if thread_id:
        if st.button("대화 쓰레드 저장"):
            save_thread(thread_id, st.session_state.messages)
        if st.button("대화 쓰레드 불러오기"):
            messages = load_thread(thread_id)
            if messages:
                for message in messages:
                    st.write(f"{message['role']}: {message['content']}")

    if st.button("저장된 대화 쓰레드 목록 보기"):
        threads = list_threads()
        st.write(threads)

    # 코드 인터프리터 기능
    code = st.text_area("코드를 입력하세요:")
    if st.button("코드 실행"):
        result = execute_code(code)
        st.write(result)

    # 팩토리에서 시스템 프롬프트를 전달하여 앱을 생성
    app = AppFactory.create_chat_app(system_prompt=system_prompt)
    
    # 대화 내용 표시
    app.display_chat()
    
    # 사용자 입력 처리 (PDF 내용 및 실시간 검색어 포함)
    app.handle_user_input(extracted_text=extracted_text)

if __name__ == "__main__":
    main()
