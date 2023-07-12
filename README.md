# Webscraping
Using beautifulsoup4 to perform web scraping

html_text=requests.get('#Link to the website').text  #.text is used to convert the data into text

header=['company_name','skill','date_posted','link_to_job'] #assigining coloum names


with open(f'#path/filename.csv','w',newline='',encoding='UTF8')as f:   #setting path to store the file and giving it a name, assigning a security codex


 job=soup.find_all('#html_tag',class_='#html_classname') #class is used to specify the specific class of li tag we want to retrive

 company_name_sample=jobs.find('h3', class_='joblist-comp-name').text.replace(' ','')  # storing data in specific objects

 writer.writerow(data) # storing the data
