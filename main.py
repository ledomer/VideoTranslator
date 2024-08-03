
import re

def main():
    with open(file='Lecture 4. Create the Project_EN.srt', mode='r', encoding='utf-8') as fsub:
        content = fsub.read()
        result = re.findall(r'(\d)\n((?:\d\d:?){3},\d{3})\s*-->\s*((?:\d\d:?){3},\d{3})\n(.+)\n', content)
        for (num, date_from, date_to, text) in result:
            print(int(num), date_from, date_to, text)



if __name__ == '__main__':
    main()
