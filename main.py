import csv
import re

def change_numb(text):
    pattern = r"(\+7|8)?\s?\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})(\s)?\(?(доб\.)?\s?(\d+)?\)?"
    result = re.sub(pattern, r"+7(\2)\3-\4-\5\6\7\8", text)
    return result


def change_file(lis):
    text_dic = {}
    for el in lis[1:]:
        keey = " ".join(" ".join(el[0:2]).split()[0:2])
        if keey not in text_dic:
            text_dic[keey] = [" ".join(el[0:2]).split()[2]] + el[3:]
        else:
            for num,i in enumerate(text_dic[keey]):
                if i == "":
                    text_dic[keey][num] = el[2:][num]
    contacts_list1 = [i.split() + text_dic[i] for i in text_dic]
    contacts_list1.insert(0, lis[0])
    return contacts_list1

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    contacts_list = change_file(contacts_list)
    for el in contacts_list[1:]:
        numb = change_numb(el[5])
        el[5] = numb
    
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=',')
        for el in contacts_list:
            datawriter.writerow(el)


