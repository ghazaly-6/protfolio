#import required libraries
import requests
from bs4 import BeautifulSoup


#Defin the target website URL
url = "https://example.com"


#Send the request to fetch the web Page
response = requests.get(url)


#Check if the Page loaded successfully
if response.status_code != 200:
    print("فشل تحميل الصفحة، الكود:", response.status_code)
    exit()


#Parse the html content using beautifulsoup
soup = BeautifulSoup(response.text, "html.parser")


#Get all text cotent from Page
all_text = soup.get_text(separator="\n", strip=True)


#Print the text on the console
print("=== النصوص المستخرجة من الصفحة ===\n")
print(all_text)


#Save The Text in file
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

print("\nتم حفظ النصوص في ملف: extracted_text.txt")