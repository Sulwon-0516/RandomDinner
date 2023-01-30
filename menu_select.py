#-*-coding:utf-8-*-

import random
import csv
import os
from typing import Optional

MENU_CSV = '저메추 - 시트1.csv'


class Menus:
    def __init__(self) -> None:
        # to allow excution on arbitrary path.
        cur_file = os.path.abspath(__file__)
        cur_dir = os.path.dirname(cur_file)
        csv_path = os.path.join(cur_dir, MENU_CSV)

        with open(csv_path, encoding='utf-8') as csvfile:
            raw_menu = csv.reader(csvfile, delimiter=',', quotechar='\n')

            # Category lists
            self.menu = {}
            self.category = []
            for menu in raw_menu:
                print(menu)
                self.menu[menu[0]] = menu[1:] 
                self.category.append(menu[0])

        self.clean_black_list()

    def forward(self) -> None:
        category = self.select_category()
        self.select_menu(category=category)

        # check whether sample again or not.
        while True:
            print("Want to sample again? (y/n)")
            sample_again = False

            ans = input()
            if ans[0] in ["y", "Y"]:
                print("sample again")
                sample_again=True
            elif ans[0] in ["n", "N"]:
                print("finish program")
                sample_again=False
            else:
                print("answer with 'y' or 'n'")
        
            if sample_again:
                self.select_menu(category=category)
            else:
                return

        
    def select_category(self) -> Optional[str]:
        print("select category (with keyboard)")
        print(f"{0}: Randomly select category")
        print(f"{1}: all category")
        ind = 2
        for categ in self.category:
            print(f"{ind}: {categ}")
            ind += 1
        print("type integer!")
        while True:
            select = input()
            try:
                select = int(select)
            except:
                print("type integer!")
                continue
            if select < ind:
                break
            else:
                print(f"type integer between 0 to {ind-1}")
        if select > 1:
            categ = self.category[select-2]
            print(f"selected {select}: {self.category[select-2]}")
        elif select == 0:
            categ = random.choices(self.category)[0]
            print(f"randomly selected category. {categ}")
        else:
            categ = None
            print(f"selected all category")
        print(f"========================================")
        return categ
        

    def select_menu(self, category=None):
        # check category
        menu_list = []
        if isinstance(category, type(None)):
            # merge ALL menus
            for categ in list(self.menu.values()):
                menu_list = menu_list + categ
            
        elif category not in self.category:
            raise NameError(f"{category} is not proper category.")
        else:
            menu_list = self.menu[category]
            

        filtered_list = []
        for menu in menu_list:
            if menu in self.black_list:
                continue
            else:
                filtered_list.append(menu)

        if len(filtered_list) == 0:
            print("there's no more menu in selected category. Please run again with different category")
            exit()

        menu = random.choices(filtered_list)[0]
        print(f"selected menu: {menu}")

        self.black_list.append(menu)

    def clean_black_list(self):
        self.black_list = []




if __name__ == '__main__':
    M = Menus()
    M.forward()
