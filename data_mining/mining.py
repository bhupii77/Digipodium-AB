from dputils.scrape import Scraper ,Tag

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


    results = scr.get_multiple_page_data(
       target = Tag(cls='_1YokD2 _3Mn1Gg'),
       items= Tag(cls='_1AtVbE col-12-12'),
       title = t,price = p ,link =l,imgurl= i
    ) 
    print(results)
    page +=1