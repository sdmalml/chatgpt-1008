import PyPDF2

def upload_and_extract_pdf(uploaded_file):
    """PDF 파일을 업로드하고 텍스트를 추출한다."""
    if uploaded_file is not None:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    return None
