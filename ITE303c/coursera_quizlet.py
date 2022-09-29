from bs4 import BeautifulSoup

files = [r"Quiz1.html", r"Quiz2.html", r"Quiz3.html", r"Quiz4.html", r"Quiz5.html", r"Quiz6.html", r"Quiz7.html",
         r"Quiz8.html",
         r"Quiz9.html", r"Quiz10.html", r"Quiz11.html", r"Quiz12.html", r"Quiz13.html", r"Quiz14.html", r"Quiz15.html",
         r"Quiz16.html",
         r"Quiz17.html", r"Quiz18.html", r"Quiz19.html", r"Quiz20.html", r"Quiz21.html", r"Quiz22.html", r"Quiz23.html",
         r"Quiz24.html",
         r"Quiz25.html", r"Quiz26.html", r"Quiz27.html", r"Quiz28.html", r"Quiz29.html", r"Quiz30.html"]

def extract_data(s):
    mydivs = s.find_all("div", {"class": "rc-FormPartsQuestion"})
    for i,div in enumerate(mydivs):
        question = div.find('div',{"data-test": 'legend'})
        answers = div.find_all('div',{"class":"rc-Option rc-Option--isReadOnly"})
        for q in question.select('p'):
            print(f"{q.text.capitalize()}")
        for j,answer in enumerate(answers):
            print(f"{chr(j+65)}: ",end="")
            for line in answer.select('p'):
                print(line.text.capitalize())
            if 'RadioChecked' in answer.find("svg")["aria-labelledby"]:
                correct = answer.select('p')
        print("---")
        for c in correct:
            print(c.text.capitalize())
        print("</>")

for file in files:
    with open(file, encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        extract_data(soup)