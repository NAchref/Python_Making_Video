import requests
from bs4 import BeautifulSoup

# Function to search Google for a question and get the top answer
def search_google_for_answer(question):
    url = "https://www.google.com/search"
    params = {
        'q': question,
        'hl': 'en',
        'num': 1,
        'ie': 'utf-8',
        'oe': 'utf-8',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    answer_div = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    if answer_div:
        return answer_div.text
    return "No relevant answer found"

# Function to get Stack Overflow questions
def get_stackoverflow_questions(tag, num_questions=5):
    url = "https://api.stackexchange.com/2.3/questions"
    params = {
        'order': 'desc',
        'sort': 'activity',
        'tagged': tag,
        'site': 'stackoverflow',
        'filter': 'default'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    questions = response.json()['items']
    
    top_questions = []
    for question in questions[:num_questions]:
        top_questions.append({
            'title': question['title'],
            'question_id': question['question_id']
        })
    
    return top_questions

if __name__ == "__main__":
    tag = "azure-virtual-machine"
    top_questions = get_stackoverflow_questions(tag)
    
    for i, question in enumerate(top_questions, 1):
        print(f"\nQuestion {i}: {question['title']}")
        google_answer = search_google_for_answer(question['title'])
        print(f"Google's Answer: {google_answer}")
