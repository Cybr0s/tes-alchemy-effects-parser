import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
# List of URLs to process
urls = [
    "https://en.uesp.net/wiki/Lore:Alchemy_A",
    "https://en.uesp.net/wiki/Lore:Alchemy_B",
    "https://en.uesp.net/wiki/Lore:Alchemy_C",
    "https://en.uesp.net/wiki/Lore:Alchemy_D",
    "https://en.uesp.net/wiki/Lore:Alchemy_E",
    "https://en.uesp.net/wiki/Lore:Alchemy_F",
    "https://en.uesp.net/wiki/Lore:Alchemy_G",
    "https://en.uesp.net/wiki/Lore:Alchemy_H",
    "https://en.uesp.net/wiki/Lore:Alchemy_I",
    "https://en.uesp.net/wiki/Lore:Alchemy_J",
    "https://en.uesp.net/wiki/Lore:Alchemy_K",
    "https://en.uesp.net/wiki/Lore:Alchemy_L",
    "https://en.uesp.net/wiki/Lore:Alchemy_M",
    "https://en.uesp.net/wiki/Lore:Alchemy_N",
    "https://en.uesp.net/wiki/Lore:Alchemy_O",
    "https://en.uesp.net/wiki/Lore:Alchemy_P",
    "https://en.uesp.net/wiki/Lore:Alchemy_R",
    "https://en.uesp.net/wiki/Lore:Alchemy_S",
    "https://en.uesp.net/wiki/Lore:Alchemy_T",
    "https://en.uesp.net/wiki/Lore:Alchemy_U",
    "https://en.uesp.net/wiki/Lore:Alchemy_V",
    "https://en.uesp.net/wiki/Lore:Alchemy_W",
    "https://en.uesp.net/wiki/Lore:Alchemy_Y",
    "https://en.uesp.net/wiki/Lore:Alchemy_Z"
]

for url in urls:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #tag_div = soup.find("div", id ="mw-content-text")
  
    # Check if 'EffectOther' class is present in the page
    has_effect_other = any(tag.has_attr('class') and 'EffectOther' in tag['class'] for tag in soup.find_all())

    if has_effect_other:
        tags = soup.find_all(class_=['mw-headline', 'EffectNeg', 'EffectPos', 'EffectOther'])
    else:
        tags = soup.find_all(class_=['mw-headline', 'EffectNeg', 'EffectPos'])

    #tags = soup.find_all(class_=['mw-headline', 'EffectNeg', 'EffectPos', 'EffectOther'])

    with open('alchemy_parsed.txt', 'a') as file:  # Open file in append mode

        # Iterate over each tag in the list
        for tag in tags:
            if 'mw-headline' in tag['class']:
                tag.string = tag.get_text() + ' NAME' # Append 'NAME' to the text content of elements with class 'mw-headline'
                print(tag.text)
                file.write(tag.text + '\n')
            if 'EffectNeg' in tag['class']:
                stripped_text = tag.get_text().strip()
                if stripped_text:  # Check if the stripped text is not empty (contains non-whitespace characters)
                    tag.string = '    ' + stripped_text
                    print(tag.text)
                    file.write(tag.text + '\n')
            if 'EffectPos' in tag['class']:
                stripped_text = tag.get_text().strip()
                if stripped_text:  # Check if the stripped text is not empty (contains non-whitespace characters)
                    tag.string = '    ' + stripped_text
                    print(tag.text)
                    file.write(tag.text + '\n')
            if 'EffectOther' in tag['class']:
                stripped_text = tag.get_text().strip()
                if stripped_text:  # Check if the stripped text is not empty (contains non-whitespace characters)
                    tag.string = '    ' + stripped_text
                    print(tag.text)
                    file.write(tag.text + '\n')