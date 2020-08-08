# Web-Scrapping using Beautifulsoup

이 프로젝트는 Algorithm Academy와 공동 프로젝트로 개발되었습니다. 이 프로젝트에서 기대되는 결과물은 정보를 얻기위한 간단한 웹 스크래핑입니다. 단계별 가이드를 보려면이 폴더의 노트북을 방문하세요. 또한 간단한 대시 보드 플라스크를 활용하여 스크랩 및 시각화 결과를 표시합니다.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

또는 다음 방법으로 requirements.txt를 설치하십시오.

```python
pip install -r requirements.txt
```


## What We Need to Do

* 노트북에서 `Beautiful soup`를 사용하여 2 개의 웹 사이트 링크를 스크랩
* 획득하고자하는 정보와 일치하는 스크래핑 프로세스로`scrap`기능을 채우십시오.

```python
table = soup.find(___)
tr = table.find_all(___)
```

* 스크랩 결과를 데이터 프레임에 저장하려면이 섹션을 채우십시오.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* 마지막으로 다음 섹션을 웹 링크로 채워 `scrap` 기능을 사용합니다.

```python
df = scrap(___) #insert url here
```

* 간단한 인터페이스로`index.html`에 UI를 설정할 수 있습니다. 

### The Final Mission

이 프로젝트에서는 아래 링크에 대한 스크랩을 예로 들어

1. 2019 년 일본 엔화에서 루피아로의 환율 데이터 `monexnews.com/kurs-valuta-asing.htm?kurs=JPY`

    * 페이지에서 얻을 수 있습니다 `sell rate`,` buy rate` and `date`
    * 2020 년 엔화 환율 변동 플롯

2. 2019 년에 출시 된 영화 데이터 `imdb.com/search/title/?release_date=2019-01-01,2019-12-31`

    * 이 페이지에서 `title`,` imdb rating`, `metascore`,` votes`, `duration` and` genre`
    * 2019 년에 가장 인기있는 7 편의 영화를 구성합니다.


