from bs4 import BeautifulSoup as bs
import requests


# base_url = 'https://www.avito.ru/rossiya/tovary_dlya_kompyutera/setevoe_oborudovanie?p={}'


def avito_pars(base_url, pages, kwords):
    item = []
    for i in range(1, pages+1):
        print(i, kwords.lower())
        print(base_url + '?q=' + kwords.lower() + '&p=' + str(i))
        request = requests.get(base_url + '?q=' + kwords.lower() + '&p=' + str(i))
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            divs = soup.find_all('div', class_='item__line')
            for div in divs:
                title = div.find('a', class_='snippet-link').text.strip('\n')
                href = 'https://avito.ru' + div.find('a', class_='snippet-link')['href']
                price = div.find('span', attrs={'itemprop': 'price'}).text.strip().replace('   ₽', '').replace(' ', '')
                img = 'https:' + div.find('img')['src']
                print('img', img)
                if kwords.lower() in title.rstrip().lower():
                    try:
                        price = int(price)
                    except ValueError:
                        price = 0
                    item.append({'title': title.rstrip(), 'img': img, 'href': href, 'price': price})
                else:
                    item.append({'title': title.rstrip(), 'img': img, 'href': href, 'price': price})
        else:
            print('ERROR')
    return item

#
# if __name__=='__main__':
#     print(avito_pars(base_url, 2, 'роутер'))
