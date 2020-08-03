# 워드 클라우드의 형태를 꾸미기 위해 기능 추가
import numpy as np

# 이미지 제어를 위해 PIL 라이브러리로부터 Image 기능 사용
from PIL import Image

# 설치한 wordcloud 외부라이브러리로부터 WordCloud 기능 사용하도록 설정
from wordcloud import WordCloud, STOPWORDS

# 설치한 matplotlib 외부라이브러리의 pyplot 기능을 사용하며, pyplot 기능을 약어로 plt로 정의
import matplotlib.pyplot as plt

# 설치한 konlpy 외부라이브러리로부터 Hannanum 기능 사용하도록 설정
from konlpy.tag import Hannanum

# 문자열(문장) 수정을 위한 파이썬 기본 기능 추가
import re

# 분석 대상 문장 / 단어별 구분자 스페이스(공백 한칸)를 이용함
# 예시 문장 : 2019년 12월, 한국폴리텍대학 서울강서캠퍼스 데이터분석과 연합뉴스
text = "연합뉴스 한국폴리텍대학 서울강서캠퍼스(학장 노정진)는 데이터분석과 2학년 김한결, 황윤영, 홍두표 학생과 1학년 김도우 학생이 " \
       "한이음 공모전에서 장려상을 받아 세종대학교에서 개최된 '소프트웨어(SW) 인재페스티벌'에 초청받았다고 10일 밝혔다. " \
       "과학기술정보통신부가 주최한 SW 인재페스티벌은 한이음 공모전 수상작에 대한 시상식이 진행됐다. " \
       "이번에 수상한 작품은 빅데이터 분석을 활용한 음성 인식 스피치 교정 애플리케이션으로 최근 블라인드 채용으로 인해 " \
       "면접에 대한 중요성이 강조되면서, 면접 교육을 위한 수강료 등 다양한 비용을 감소시키기 위해 개발한 소프트웨어다. " \
       "사용자는 태블릿, 스마트폰과 같은 스마트 기기로부터 면접 질문을 받아 마이크에 음성으로 면접 질문에 대해 대답하고, " \
       "소프트웨어는 그 대답에 대한 분석을 진행한다. 분석 내용은 자주 사용하는 명사 단어, 목소리의 높낮이, 목소리 빠르기, " \
       "긍정·부정 단어 사용 여부 등이며, 분석을 위해 한글 형태소 분석, 음성인식(TTS), 오피니언 마이닝 등 기술이 적용됐다."

# myHannanum 변수에 Hannanum 기능을 넣어줌
myHannanum = Hannanum()

# 단어 분석의 정확도를 높이기 위해 특수문자 제거
# 특수문자는 키보드 상단 숫자패드의 특수문자가 발견되면 한칸 공백으로 변경
replace_text = re.sub("[!@#$%^&*()_+]", " ", text)

# 특수문자가 제거된 문장 출력
print(replace_text)

# 명사 분석 결과는 여러 단어들이 저장된 배열형태로 데이터를 생성하기 때문에 배열을 문자열로 변경하기위해
# join 함수를 사용하며, analysis_text 변수에 문자열로 변환된 결과를 저장함
analysis_text = (" ".join(myHannanum.nouns(replace_text)))

# stopwords 변수에 원하지 않는 단어들 추가
stopwords = set(STOPWORDS)
#stopwords.add("분석")
#stopwords.add("소프트웨어")

# 워드 클라우드 형태 이미지 가지오기
myImg = np.array(Image.open("myImage.png"))

# 워드 클라우드를 생성하며, 생성된 워드 클라우드를 myWC 이름의 변수에 저장하기
# 워드 클라우드를 표시하는 단어가 한글일 경우, 파이썬에서 인식 불능 현상이 발생할 수 있기 때문에 글꼴을 강제 설정함
myWC = WordCloud(font_path="font/NanumGothic.ttf", mask=myImg, stopwords=stopwords, background_color="white").generate(analysis_text)

# 워드 클라우드의 크기 정의
plt.figure(figsize=(5, 5))

# 워드 클라우드의 이미지의 부드럽기 정도
plt.imshow(myWC, interpolation="lanczos")

# x, y축에 기본 숫자들 제거
plt.axis('off')

# 워드 클라우드 보여주기
plt.show()


