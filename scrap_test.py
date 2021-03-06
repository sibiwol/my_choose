import requests
from bs4 import BeautifulSoup
# URL을 읽어서 HTML를 받아오고,
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
        author_span = divs[1]
        img_a = divs[0]
        # div[1]>p[1]>span[1]author
        # div[0]>a>img
        title = title_div.find('p').find('a')
        book = {}
        if title is not None:
            # print('<제목여기>')
            # print(title.text)
            book['title'] = title.text
        author = author_span.find('p').find('span').find('span')
        # 37오류 AttributeError: 'NoneType' object has no attribute'find'
        if author is not None:
            book['author'] = author.text
            print('<작가여기>')
            print(author.text)
        content = content_div.find('p')
        if content is not None:
            # print('<콘텐트여기>')
            # print(content.text)
            book['content'] = content.text
        img = img_a.find('a').find('img')
        if img is not None:
            book['img'] = img.img
            print('<표지여기>')
            print((img.img))
        if len(book) > 0:
            books.append(book)
    if len(books) > 0:
        return books
    else:
        return None

result = get_book_info(1)
# print('첫 페이지 결과')
print(result)
# 위 코드 확인



# 업데이트
# # 오타가 많으니 이 줄을 복사해서 씁시다!
# db.dbchoose_test.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
# user = db.dbchoose_test.find_one({'name': '덤블도어'})
# print(user)
#
# 삭제
# db.dbchoose_test.delete_all()
#
# user = db.dbchoose_.find_all()
# print(user)




