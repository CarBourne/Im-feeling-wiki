
import webbrowser
from time import sleep

from playwright.sync_api import sync_playwright
import random as rand





def pick_a_number():
    number1 = input("Pick a number 1-10: ")
    number2 = input("Pick another number 1-10: ")
    if (int(number1)>10) and (int(number2)>10):
        print("not valid")
        return
    if (int(number1)<0) and (int(number2)<0):
        print("not valid")
        return
    else:
        output1 = int(number1)
        output2 = int(number2)
        return (output1, output2)

        
    

def im_feeling_wiki(output1,output2):
  with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    
    
    visited = set()
    
    for i in range(output1):
      print("iteration #", i, "here's the list:")
      links = page.query_selector_all("p a")
      # print(links)
      number_link = links[output2]
      
      


      link_url = number_link.get_attribute("href")

      if "Help" in link_url:

        output2+=1
        number_link = links[output2]
        link_url = number_link.get_attribute("href")

        print("Found word exception going to the next item")
        
      elif "cite_note" in link_url:
        output2+=1
        number_link = links[output2]
        link_url = number_link.get_attribute("href")

        print("Found word exception going to the next item")
        
        # continue
      elif link_url in visited:
        output2+=1
        number_link = links[output2]
        link_url = number_link.get_attribute("href")

        print("Found duplicate exception going to the next item")
        continue
      
      
      elif len(links) < output2:
        
        print("The number is too big selecting the biggest number available: ")
        print((len(links)))
        number_link = links[(len(links))]
        
        
      else:
            visited.add(link_url)
      
      url = "https://en.wikipedia.org" + link_url
      page.goto(url)

      webbrowser.open(url)
    
############################# safety checks

########################################
    
    
    page.close()

def main():
  number1, number2 = pick_a_number()
  im_feeling_wiki(number1, number2)


main()