import requests

def search_web(query):
    """Tavily API를 사용하여 실시간 웹 검색을 수행한다."""
    api_key = "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"  # 발급받은 Tavily API 키
    url = "https://api.tavily.io/v1/search"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    params = {
        "query": query,
        "limit": 10  # 검색 결과 제한 (예: 10개)
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json().get("results", [])
    return None
