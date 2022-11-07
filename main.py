import requests
from bs4 import BeautifulSoup

print("hello world")

url = "https://rhineforecast.com/kaub/"
#url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
print(soup.prettify())
results = soup.find_all('figure',class_="figure")
results = soup.find_all('img',class_="figure-img img-fluid rounded")
print("here1")
for result in results:
  print(result.prettify())
print("here 2")

#print(results.prettify())
# job_elements = results.find_all("div", class_="figure-img")

# for job_element in job_elements:
#   print(job_element, end="\n"*2)


images = soup.select('img')
# images_url = images[0]['src']
# print(images_url)
# images_url = images[1]['src']
# print(images_url)
print(len(images))
for i in range(0,len(images),1):
  print(images[i]['src'])

image_data = requests.get(images[17]['src']).content
with open('pic.jpg', 'wb') as handler:
  handler.write(image_data)
print("looking")
a = soup.body.select('img', text="kaub")
i = 0
for a1 in a:
  print("find ", i)
  print(a1)
  print("parent")
  print(a1.parent)
  # print(a1.parent['src'])
  i+=1