import os
import time
import arxiv
from langchain_community.vectorstores import Qdrant
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
import json, requests, datetime, arxiv, time
from io import BytesIO
from PyPDF2 import PdfReader

pplx_key = ''

def get_yesterday_date():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    formatted_yesterday = yesterday.strftime('%Y-%m-%d')
    return formatted_yesterday

def get_daily_papers():
    yesterday_date = get_yesterday_date()
    response = requests.get(f"https://huggingface.co/api/daily_papers?date={yesterday_date}")
    if response.status_code == 200:
        print("meow")
    else:
        print(f"Request failed with status code {response.status_code}")
    return response.text

def get_paper_titles():
    paper_titles = []
    data = get_daily_papers()
    papers = json.loads(data)
    for paper in papers:
        title = paper["paper"]["title"]
        print(title)
        paper_titles.append(title)
    return paper_titles

def save_papers(dirpath):

    paper_titles = get_paper_titles()

    for paper_title in paper_titles:
        # Search arXiv for papers related to "LLM"
        client = arxiv.Client()
        search = arxiv.Search(
            query=paper_title,
            max_results=1,
            sort_order=arxiv.SortOrder.Descending
        )

        # Download and save the papers
        for result in client.results(search):
            while True:
                try:
                    result.download_pdf(dirpath=dirpath)
                    print(f"-> Paper id {result.get_short_id()} with title '{result.title}' is downloaded.")
                    break
                except (FileNotFoundError, ConnectionResetError) as e:
                    print("Error occurred:", e)
                    time.sleep(1)

def papers_to_text(dirpath):

    # Load papers from the directory
    papers = []
    loader = DirectoryLoader(dirpath, glob="./*.pdf", loader_cls=PyPDFLoader)
    try:
        papers = loader.load()
    except Exception as e:
        print(f"Error loading file: {e}")
    print("Total number of pages loaded:", len(papers)) 

    # Concatenate all pages' content into a single string
    full_text = ''
    for paper in papers:
        full_text += paper.page_content

    # Remove empty lines and join lines into a single string
    full_text = " ".join(line for line in full_text.splitlines() if line)
    print("Total characters in the concatenated text:", len(full_text)) 

    return full_text

def llm_talkr(papers_text):
        
        prompt = f"""Below is the text of few Arxiv papers in the area of Arificial Intelligence, Machine Learning and Large Language Models.
        Summarize these papers and explain their main ideas and how these ideas can affect modern AI and technology world.
        If papers don't have any significant achievements, just say that these papers don't have anything special, but still summarize them in few sentences.
        {papers_text}""" 

        url = "https://api.perplexity.ai/chat/completions"
        payload = {
            "model": "llama-3.1-70b-instruct",
            "temperature": 0.5,
            "messages": [
                {
                    "role": "system",
                    "content": 'You are an expert machine learning scientist and a professor, you read Arxiv papers and summarize them for the average people.'
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer " + pplx_key
        }
        response = requests.post(url, json=payload, headers=headers)
        json_data = response.text
        parsed_json = json.loads(json_data)
        answer_content = parsed_json["choices"][0]["message"]["content"]
        answer = bytes(answer_content, 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')

        return answer

def main():
    # Create directory if not exists
    dirpath = "arxiv_papers"
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    
    save_papers(dirpath)

    print('\n\n\n>>>>>>>>>>>>>> PAPERS SAVED\n\n\n')
    
    papers_text = papers_to_text(dirpath)

    answer = llm_talkr(papers_text)

    print(answer)

if __name__ == '__main__':
    main()