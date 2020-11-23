import bs4, requests

def getAmazonPrice(productUrl): # Take in the URL of the Amazon page
    headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#buyNewSection > div.a-section > div.a-row > span.inlineBlock-display > span')
    title = soup.select('#productTitle')
    return elems[0].text.strip(), title[0].text.strip() # Return two answers: price, title


x = input('Enter a URL:')

price, title = getAmazonPrice(x)
print('The price of "' + title + '" is ' + price + '.')
