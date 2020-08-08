# Web-Scrapping using Beautifulsoup

This project was developed as a collaborative project with the Algorithm Academy. The deliverables expected from this project are simple webscrapping to obtain information. For a step by step guide, visit the notebook on this folder. We'll also take advantage of a simple dashboard flask to display our scrap and visualization results.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Or simply install requirements.txt in the following way

```python
pip install -r requirements.txt
```


## What We Need to Do

* scraping 2 website links using `beautiful soup` on the notebook
* Fill in the `scrap` function with the scraping process that matches the information you want to obtain

```python
table = soup.find(___)
tr = table.find_all(___)
```

* Fill in this section to save the scrap results into a dataframe.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Finally, use the `scrap` function by filling in the following section with a web link.

```python
df = scrap(___) #insert url here
```

* We can set the UI on `index.html` with a simple interface. 

### The Final Mission

In this project, we do scrapping for those link below as an example

1. Data on the exchange rate of Japan Yen to rupiah in 2019 from `monexnews.com/kurs-valuta-asing.htm?kurs=JPY`

    * From the page you can get `sell rate`,` buy rate` and `date`
    * Make a plot of JPY exchange rate movement in 2020

2. Movie data released in 2019 from `imdb.com/search/title/?release_date=2019-01-01,2019-12-31`

    * From this page get `title`,` imdb rating`, `metascore`,` votes`, `duration` and` genre`
    * plot the 7 most popular films in 2019.


