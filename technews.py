import requests
import bs4


#Create a response object from the target website
res = requests.get('https://www.theverge.com/tech')  
#parse the html to a beautiful soup object 
soup = bs4.BeautifulSoup(res.text , features = "html.parser")

#identify the box where top tech news are housed
news_box = soup.find('div',{'class': 'c-compact-river'})
#identify all the headlines from the news_box in a list
news_list = news_box.find_all('h2',{'class': 'c-entry-box--compact__title'})

#print all the news headlines from the news list
for news in news_list:
	print(news.text)
	print()

#Wait untill the user presses enter
input()	