from django.shortcuts import render
import requests
import datetime
import requests
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'indore')
    else:
        city = 'indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=96fad655d70c46308d8bc43a97b7dafa'
    PARAMS = {'units': 'metric'}

    API_KEY='AIzaSyDO_u96k9emA8iysZBZtuK9lzUmivRTOPQ'
    SEARCH_ENGINE_ID='e12cfca6594a648d9'

    query=city+"1920*1080"
    page=1
    start = (page - 1) * 10 + 1
    searchType='image'
    
    

    city_url=f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    





    try:
          
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
         
          day = datetime.date.today()

          return render(request,'index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
               
    
     
