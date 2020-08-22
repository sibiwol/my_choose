from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbchoose_test # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


# @app.route('/')
# def home():
#     return render_template('index.html')

#서버코드
@app.route('/search', methods=['POST'])
def post_novels():
#     # 1. 클라이언트로부터 데이터를 받기
#     # 2. 스크래핑하기
    url = 'http://www.joara.com/literature/view/book_list.html'
    def get_book_info(page_no):
    paginated_url = 'http://www.joara.com/literature/view/book_list.html?page_no=' + str(
        page_no) + '&bookpart=&sl_type=&sl_chkcost=&sl_category=&sl_search=&sl_keyword=&sl_chk=&sl_minchapter=&sl_maxchapter=&sl_redate=&sl_orderby=&sl_othercategory=&list_type=normal&sub_category='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(paginated_url, headers=headers)
    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')
    # select를 이용해서, tr들을 불러오기
    table = soup.select('#content > section > table')
    trs = table[0].find_all('tr')
    books = []
    for tr in trs:
        td = tr.find('td')
        if td is None:
            content
        divs = td.find_all('div')
        if len(divs) < 2:
            # title, content 없음
            continue
        title_div = divs[0]
        content_div = divs[1]
        title = title_div.find('p').find('a')
        book = {}
        if title is not None:
            # print('<제목여기>')
            # print(title.text)
            book['title'] = title.text
        content = content_div.find('p')
        if content is not None:
            # print('<콘텐트여기>')
            # print(content.text)
            book['content'] = content.text
        if len(book) > 0:
            books.append(book)
    if len(books) > 0:
        return books
    else:
        return None

result = get_book_info(1)

    # 3. mongoDB에 데이터를 넣기
db.dbchoose_test.insert_many(result)

# return jsonify({'result': 'success'})
#
#
# @app.route('/memo', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
#     result = list(db.articles.find({}, {'_id': 0}))
#     # 2. articles라는 키 값으로 article 정보 보내주기
#     return jsonify({'result': 'success', 'articles': result})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)