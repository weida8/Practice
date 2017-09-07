from lxml import html
import requests
def main():

	page = requests.get("http://econpy.pythonanywhere.com/ex/001.html")
	tree = html.fromstring(page.content)

	buyers = tree.xpath('//div[@title="buyer-name"]/text()')
	prices = tree.xpath('//span[@class="item-price"]/text()')
	print( "buyers: ", buyers)
	print( "prices: ", prices)
main()