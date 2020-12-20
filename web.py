import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


all_years = []
all_mil = []
all_price = []

for i in range(1,115):
    print(i)
    my_url = f'https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cb=40&cbl1=6&cg=1020&mys=2010&page={i}&ps=2'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class":"styled__Wrapper-sc-1kpvi4z-0 itHtzm"})

    for cont in containers:
        try:
            attributes = cont.findAll("li", {"class":"ParametersList__ListItem-sc-18ndpo4-2 bQxiZq"})
            year = int(''.join(c for c in attributes[0].text if c.isdigit()))
            mil = int(''.join(c for c in attributes[2].text.split("-")[1] if c.isdigit()))
            price_str = cont.find("div", {"TextSubHeading__TextSubHeadingWrapper-sc-1ilszdp-0 bcaUdR Price__Wrapper-sc-1v2maoc-0 bNwNaE"})
            price = int(''.join(c for c in price_str.text.split("(")[0] if c.isdigit()))
            
            all_years.append(year)
            all_mil.append(mil)
            all_price.append(price)
        except IndexError:
            print(attributes[2].text)


import matplotlib.pyplot as plt
print(len(all_price))

plt.plot(all_years,all_price,'.')
plt.show()
