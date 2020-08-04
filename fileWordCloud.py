# 설치한 wordcloud 외부라이브러리로부터 WordCloud 기능 사용하도록 설정
from wordcloud import WordCloud, STOPWORDS

# 설치한 matplotlib 외부라이브러리의 pyplot 기능을 사용하며, pyplot 기능을 약어로 plt로 정의
import matplotlib.pyplot as plt

# 설치한 konlpy 외부라이브러리로부터 Hannanum 기능 사용하도록 설정
from konlpy.tag import Hannanum

# 문자열(문장) 수정을 위한 파이썬 기본 기능 추가
import re

# 분석 대상 문장 / 단어별 구분자 스페이스(공백 한칸)를 이용함
text = open("contents.txt", encoding="UTF-8").read()

print(text)

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
# stopwords.add("분석")
# stopwords.add("소프트웨어")

# 워드 클라우드를 생성하며, 생성된 워드 클라우드를 myWC 이름의 변수에 저장하기
# 워드 클라우드를 표시하는 단어가 한글일 경우, 파이썬에서 인식 불능 현상이 발생할 수 있기 때문에 글꼴을 강제 설정함
myWC = WordCloud(font_path="font/NanumGothic.ttf", stopwords=stopwords, background_color="white").generate(analysis_text)

# 워드 클라우드의 크기 정의
plt.figure(figsize=(5, 5))

# 워드 클라우드의 이미지의 부드럽기 정도
plt.imshow(myWC, interpolation="lanczos")

# x, y축에 기본 숫자들 제거
plt.axis('off')

# 워드 클라우드 보여주기
plt.show()


