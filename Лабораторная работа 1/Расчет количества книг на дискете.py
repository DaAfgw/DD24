# TODO Найдите количество книг, которое можно разместить на дискете
simb1 = 4
simb_str = 25
str_page = 50
page_book = 100
b1= simb1 * simb_str * str_page * page_book
disk = 1.44 * 1024 * 1024 #переводим Мб в байты
print("Количество книг, помещающихся на дискету:", round(disk / b1))
