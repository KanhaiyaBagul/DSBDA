req = requests.get('https://books.toscrape.com/catalogue/page-1.html')

print(req)

soup = bs4.BeautifulSoup(req.text)
soup

soup.select('article')

soup.select('article h3 a')

len(soup.select('article h3 a'))

soup.select('article h3 a')

soup.select('article h3 a')[0]

soup.select('article h3 a')[0]['title']

soup.select('article p')

soup.select('article p')[0]

soup.select('article p')[0]['class']

soup.select('article p')[1]

soup.select('article p')[1]

soup.select('article p')[1].string

soup.select('article p')[1].string.replace('Â£','')

title_list =[]
rating_list = []
price_list = []

for pg_num in range(1,51):
  req = requests.get(f'https://books.toscrape.com/catalogue/page-{pg_num}.html')
  soup_pg = bs4.BeautifulSoup(req.text)
  
  for item in soup_pg.select('article h3 a'):
    title_list.append(item['title'])
  
  for n in range(0,60,3):
     rating_list.append(soup_pg.select('article p')[n]['class'][1])
  
  for n in range(1,60,3):
     price_list.append(soup_pg.select('article p')[n].string.replace('Â£',''))


# price_list

dic = dict(zip(title_list,zip(rating_list, price_list)))
df = pd.DataFrame.from_dict(dic, orient='index')
df

# we already know the url
soup.select('article h3 a')

nreq= requests.get('https://books.toscrape.com/catalogue/in-her-wake_980/index.html')


nsoup = bs4.BeautifulSoup(nreq.text)
nsoup

nsoup.select('tr')

nsoup.select('tr th')

nsoup.select('tr td')

nsoup.select('tr td')[2].text



new_df = pd.DataFrame()  # empty dataframe
index_num= 0             # index of dataframe

for pg_num in range(1,51):
  req = requests.get(f'https://books.toscrape.com/catalogue/page-{pg_num}.html')
  soup_pg = bs4.BeautifulSoup(req.text)
  book_info_list = soup_pg.select('article h3 a')   # all books on that page    # values of that features

  for n in range(0,20):
      res = requests.get('http://books.toscrape.com/catalogue/'+ book_info_list[n]['href']) # url of each book in above page
      soup = bs4.BeautifulSoup(res.text, 'lxml')
      
      book_features_column_list = soup.select('tr th')   # book features like price, rating of each book
      book_column_values = soup.select('tr td')          # values of that features
      
      column_names = [ item.text for item in book_features_column_list ]
      
      column_values = [item.text for item in book_column_values ]
      
      d = dict(zip(column_names, column_values))  # making dictionary with features as columns and values as rows
  
      df = pd.DataFrame(d, index = [index_num + n]) 
      new_df = new_df.append(df)   # append df of every page
      
  index_num += 20  # index for each page to be incremented by 20 as zero_base index since there are 20 books on each page 
  


new_df

# adding new columns in a dataframe 
new_df["Rating"] = rating_list
new_df["Title"] = title_list
new_df

