from dputils.scrape import Scraper ,Tag
from sqlalchemy.orm import sessionmaker
from orm import Product, create_engine
all_results=[]

page = 1
query = 'laptops'
limit = 5

for i in range (1,limit+1):
   url = f'https://www.flipkart.com/search?q={query}&page={limit}'

   print(url)

   #create a scraper object 
   scr = Scraper(webpage_url=url)

   t=Tag(cls='_4rR01T')
   p=Tag(cls='_30jeq3 _1_WHN1') 
   l=Tag('a',cls = '_1fQZEK', output='href')
   i = Tag('img',cls ='_396cs4',output= 'src')


   results = scr.get_repeating_page_data(
      target = Tag(cls='_1YokD2 _3Mn1Gg'),
      items= Tag(cls='_1AtVbE col-12-12'),
      title = t,price = p ,link =l,imgurl= i
   ) 
   page += 1
   if len(results) == 0:
      print('No more results')
      break
   all_results += results

if len(all_results) > 0:
   engine = create_engine('sqlite:///mining.db', echo=True)
   Session = sessionmaker(bind=engine)
   db = Session() # will create a session object
   for record in all_results:
      p = Product(title = record['title'],
                  price = record['price'],
                  url = record['link'],
                  imgurl = record['imgurl'])
      db.add(p)
      print("🌀 Record added")
   db.commit() # save all the records
   db.close() # close the connection