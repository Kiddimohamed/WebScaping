import time

from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import pandas as pd
import plotly.express as px


'''
with open('name', 'r') as variableName:
    content = variableName.read()
    print(content)

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
    tags = soup.find('h4') # find_all to find all the tags in  list form
    print(tags)
    
    # Give us the first H5 tags and its content
    print(tags.text)
    # in case we use find all we have a list then we should iterate from the list using for loop
    course_cards = soup.findAll('div', class_='divname')
    for course in course_cards:
        course_name = course.h5.text
        # the cotent of <a> is star from 20$ so we need just the last word
        course_price = course.a.text.split()[-1]
        print('for the ' + course_name + ' : ' + course_price)
        print(f' {course_name} costs {course_price}')
'''
#TODO NOMBRE FILM / ANNE
def film_details():
    html_text_250 = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
    soup = BeautifulSoup(html_text_250, 'lxml')
    film = np.array([['Classement', 'Name', 'Date', 'Rating', 'auteur']])
    #tbody=soup.find_all('tbody', class_ = 'lister-list')
    titleColumns=soup.find_all('td', class_ = 'titleColumn')
    ratings=soup.find_all('td', class_ = 'ratingColumn imdbRating')
    for titleColumn,rating in zip(titleColumns,ratings):
        auteur = titleColumn.a['title'].split('(dir.)')[0]
        classement=titleColumn.text.replace('\n','').split()[0]
        name=titleColumn.find('a').text.replace('\n','')
        date=titleColumn.find('span', class_ = 'secondaryInfo').text.replace('\n','')
        rat=rating.find('strong').text
        # print(f' {classement} {name} {date} {rat}')

        ls=np.array([classement,name,date,rat,auteur])
        #  print(ls)
        film=np.append(film,[ls],axis=0)
    print(film)
    frame=pd.DataFrame(film[1:],columns=film[0])
    print(frame.head())
    df = px.frame.gapminder().query("country == 'Canada'")
    fig = px.bar(df, x='year', y='pop',
                 hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
                 labels={'pop': 'population of Canada'}, height=400)
    fig.show()


#film_details()

if __name__ == '__main__':
    while True:
        film_details()
        time_wait = 10
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait*60)















