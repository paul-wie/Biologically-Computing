from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/N24')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
print(tree)
