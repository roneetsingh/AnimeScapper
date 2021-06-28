import os

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print('Some modules are not installed! Installing them automatically.')
    os.system('python -m pip install -r requirements.txt')

title = []
link = []

def about(link):
    source_code = requests.get("https://www10.gogoanime.io"+link)
    content = source_code.content
    soup = BeautifulSoup(content,'html.parser')
    container_soup = soup.find('div', {'class':'anime_info_body_bg'})
    print("\nName of the Anime : ", container_soup.find('h1').getText(),"\n") 
    titles_detail = container_soup.find_all('p',{'class':'type'})
    for elem in titles_detail:
        print(elem.getText())
        print("\n")

def getdetails(soup):
    raw_soup = soup.find_all('div', {"class":'img'})
    for item in raw_soup:
        temp_soup = item.find('a')
        title.append(temp_soup['title'])
        link.append(temp_soup['href'])

def getlinks(title,link):
    for i in range(len(title)):
        print("%d. %s : https://www10.gogoanime.io%s\n" % (i+1,title[i],link[i]))

def newanime():
    anime_name = input("[+] Enter the name of the Anime : ")
    search_url = ("https://www10.gogoanime.io//search.html?keyword=" + anime_name)
    source_code = requests.get(search_url)
    content = source_code.content
    global soup
    soup = BeautifulSoup(content,features="html.parser")
    choice = input("[+] Do you want Details or Anime Links? (details/links) : ")
    if choice.lower() == "details":
        getdetails(soup)
        about(link[0])
    elif choice.lower() == "links":
        getdetails(soup)
        getlinks(title,link)
    else:
        print("[-] Enter a valid choice.")

if __name__ == "__main__":
    newanime()


