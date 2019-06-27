while True:
    food_list = ['apple', 'pineapple', 'mango']
    print("this is your current food list:", *food_list, sep=' | ')
    change = input('''would you like to change anything in your food list? 
    yes / no ''')
    if change == "yes":
        what_change = input('''what would you like to do?
        update item / add item / delete item / read list / cancel ''')
        if what_change == "add item":
            add_what = input("what would you like to add? ")
            food_list.append(add_what)
            print('''this is your new food list:
            ''', *food_list, sep=' | ')
        elif what_change == "update item":
            update_where = int(input("where would you want to update? "))
            update_what = input("what would you like to change? ")
            food_list[update_where] = update_what
            print('''this is your new food list:
            ''', *food_list, sep=' | ')
        elif what_change == "delete item":
            del_item = int(input("where would you like to delete? "))
            food_list.pop(del_item)
            print('''this is your new food list:
            ''', *food_list, sep=' | ')
        elif what_change == "cancel":
            print("canceled")
        elif what_change == "read list":
            print('''this is your current list:
            ''', *food_list, sep=' | ')
        else:
            print("please choose one of the given action")
    elif change == "no":
        print("ok")
    else:
        print("please choose one of the given action")
    break