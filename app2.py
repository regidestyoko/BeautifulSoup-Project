from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')
app = Flask(__name__)

def scrap(url):
    #This is fuction for scrapping
    #This is fuction for scrapping
    url_get = requests.get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31')
    imdb = BeautifulSoup(url_get.content,"html.parser")

    #Find the key to get the information
    imdbtable = imdb.find('div', attrs={'class':'lister-list'}) 
    spec = imdbtable.find_all('div', attrs={'class':'lister-item-content'}) 

    predf = [] #initiating a tuple

    
    for i in range(0, len(spec)):
        row = imdbtable.find_all('div', attrs={'class':'lister-item-content'})[i]

        #get title
        title = row.find('h3', attrs={'class':'lister-item-header'}).find('a').text
        title = title.strip() #for removing the excess whitespace

        #get rating
        rating = row.find('div', attrs={'class':'inline-block ratings-imdb-rating'}).text
        rating = rating.strip() #for removing the excess whitespace
        
        #get vote
        vote = row.find('span', attrs={'name':'nv'}).text
        vote = vote.strip() #for removing the excess whitespace

        try :
            #get metascore
            metascore = row.find('span', attrs={'class':'metascore favorable'}).text
            metascore = metascore.strip() #for removing the excess whitespace
        except:
            metascore = np.nan
        
        try :
            #get duration
            dur = row.find('span', attrs={'class':'runtime'}).text
            dur = dur.strip() #for removing the excess whitespace
        except:
            dur = np.nan
            
        try :
            #get certification
            certification = row.find('span', attrs={'class':'certificate'}).text
            certification = certification.strip() #for removing the excess whitespace
        except:
            certification = np.nan

        try :
            #get certification
            genre = row.find('span', attrs={'class':'genre'}).text
            genre = genre.strip() #for removing the excess whitespace
        except:
            genre = np.nan
    
        predf.append((title,rating,metascore,vote,dur,certification,genre))

    predf = predf[::-1] #remove the header

    df = pd.DataFrame(predf, columns =('title','rating','metascore','vote','duration','certification','genre')) #creating the dataframe
   #data wranggling -  try to change the data type to right data type
    df.vote = df.vote.apply(lambda x : x.replace(',','.')).astype('float64')
    df.rating = df.rating.astype('float64')
    df.metascore = df.metascore.astype('float64')
    
    return df

@app.route("/")
def index():
    df = scrap('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31') #insert url here
    #creating plot
    drama = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Drama).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    action = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Action).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    adventure = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Adventure).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    comedy = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Comedy).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    crime = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Crime).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    mystery = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Mystery).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    scifi = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Sci-Fi).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    family = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Family).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    thriller = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Thriller).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    romance = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Romance).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    biography = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Biography).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    horror = pd.concat([df,df.genre.str.extract('.*(?P<Genres>Horror).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    war = pd.concat([df,df.genre.str.extract('.*(?P<Genres>War).*')],axis=1).groupby('Genres').agg({'rating':'mean','title':'count'}).reset_index()
    su = pd.concat([drama,action,adventure,comedy,crime,mystery,scifi,family,thriller,romance,biography,horror,war]).reset_index().drop(columns='index')
    summary = su.rename(columns={'title':'Count of Title'})
    summary['Count of Title'] = summary['Count of Title'].astype('int64')
    sumsortrat = summary.sort_values('rating',ascending=False)

    #This part for rendering matplotlib
    fig = plt.figure(figsize=(11,9),dpi=300)
    fig.add_subplot()
    plt.xticks(rotation=30)
    plt.rcParams.update({'font.size': 100})
    plt.ylabel('Average Rating')
    plt.xlabel('Genres')
    plt.bar(sumsortrat.Genres,sumsortrat.rating)
    # df.plot()
    
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    fig = plt.figure(figsize=(11,9),dpi=300)
    fig.add_subplot()
    plt.xticks(rotation=30)
    plt.ylabel('Count Of Title')
    plt.xlabel('Genres')
    plt.bar(sumsortrat.Genres,sumsortrat['Count of Title'])

    plt.savefig('plot2',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result2 = str(figdata_png)[2:-1]
    
    #this is for rendering the table
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index2.html", table=df, result=result, result2=result2)


if __name__ == "__main__": 
    app.run()
