import  requests

def fetch_api_data(url):
    response = requests.get(url)
    content  = response.json()
    return content
