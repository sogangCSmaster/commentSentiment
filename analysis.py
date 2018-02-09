import NCS
from textblob import TextBlob
from googletrans import Translator

url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002381762'


#댓글 감성 분석
def commentSentiment(url):
    translator = Translator()
    totalPos = 0
    totalNeg = 0

    comments = NCS.NNCS(url)
    
    for comment in comments:
        transEng = translator.translate(comment, src='ko')
        transEng = transEng.text
        analysis = TextBlob(transEng)
        polarity = analysis.sentiment.polarity
        
        if polarity >=0:
            totalPos = totalPos + 1
        else:
            totalNeg = totalNeg + 1
    
    #할일...
    #영화 평점 학습 모델과
    #쇼핑몰 평점 학습 모델을 붙여서 정확도를 높이자.

    
    if totalPos > totalNeg:
        return "positive"
    else:
        return "negative"
