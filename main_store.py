def read_from_database():
    try:
        products = []
        f = open("database.csv", "r")

        big_text = f.read()
        products_list = big_text.split('\n')

        for i in range(len(products_list)):
            info = products_list[i].split(',')
            products.append({'id': info[0], 'name': info[1], 'price': info[2], 'count': info[3]})

    except Exception as e:
        print(e)
        products = []

    return products


def add():
    id = input('enter id: ')
    name = input('enter name: ')
    price = input('enter price: ')
    count = input('enter count: ')
    products.append({'id': id, 'name': name, 'price': price, 'count': count})
    print('your product add to database successfully')


def search():
    use_input = input('Enter a id or name to search= ')
    for product in products:
        if product['id'] == use_input or product['name'] == use_input:
            print(product)
            break
    else:
        print('you product not found')


def edit():
    show_all()
    use_input = input('Enter a id or name to edit= ')
    for product in products:
        if product['id'] == use_input or product['name'] == use_input:
            print(product)
            break
    else:
        print('you product not found')

    products.remove(product)
    id = input('Enter edited id: ')
    name = input('Enter edited name: ')
    price = input('Enter edited price: ')
    count = input('Enter edited count: ')
    products.append({'id': id, 'name': name, 'price': price, 'count': count})
    print('your product edited successfully')


def remove():
    show_all()
    use_input = input('Enter a product id or name to edit= ')
    for product in products:
        if product['id'] == use_input or product['name'] == use_input:
            print(product)
            break
    else:
        print('you product not found')
    products.remove(product)
    print('your product removed successfully')


def buy():
    receipt = []
    price = int()

    while True:
        user_list = input('Do you still want to buy? (y or n): ')
        if user_list == 'y':
            print('Choose your product want to buy from the list blew')
            for product in products:
                print(product)
            use_input = input('enter product you want= ')
            for product in products:
                if product['id'] == use_input or product['name'] == use_input:
                    print(product)
                    break
            else:
                print('This product is out of stock')
                exit()
            print('We have', product['count'], 'number of this product how much do yo want? ')
            num_user = int(input())
            c = int(product['count'])
            if num_user > c:
                print('The number of you want is out of stock please try again')
            elif num_user <= c:
                receipt.append({'id': product['id'], 'name': product['name'], 'price': product['price'],
                                'count': product['count']})
                count = int(product['count']) - num_user
                products.remove(product)
                products.append({'id': product['id'], 'name': product['name'], 'price': product['price'], 'count': str(count)})
                price += int(num_user) * int(product['price'])

        elif user_list == 'n':
            print(receipt)
            print('Your Total cost is: ', price)
            break

        else:
            print('your input is not correct')


def show_all():
    for product in products:
        print(product)


def show_menu():
    print('Welcome to store')
    print('1- add new products')
    print('2- search')
    print('3- edit')
    print('4- remove')
    print('5- buy')
    print('6- show all')
    print('7- Exit')


products = read_from_database()
# print(products)


while True:
    show_menu()
    choice = int(input('enter your choice: '))

    if choice == 1:
        add()

    elif choice == 2:
        search()

    elif choice == 3:
        edit()

    elif choice == 4:
        remove()

    elif choice == 5:
        buy()

    elif choice == 6:
        show_all()

    elif choice == 7:
        choice = input('Would you like to save your change in database? (y or n): ')
        if choice == 'y':
            f = open("database.csv", "w")
            for product in products:
                f.write(str(product['id']+','+product['name']+','+product['price']+','+product['count']))
                exit()