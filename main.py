from program_data import resources, MENU


def selection(select_product):
    a = None
    for i in MENU:
        if i == select_product:
            a = MENU[i]["ingredients"]
    if a == None:
        a = 'report'
    return a


def check_resources(resources_total, select_product_resource):
    for i in select_product_resource:
        if resources_total[i] < select_product_resource[i]:
            a = i
            break
        else:
            a = 'ok'
    return a


money_total = 0
left_resources = resources
is_on = True

while is_on:
    select_product = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if select_product == 'off':
        is_on = False
    ingr_of_select_product = selection(select_product)

    if ingr_of_select_product != 'report':

        a = check_resources(left_resources, ingr_of_select_product)

        if check_resources(left_resources, ingr_of_select_product) != 'ok':
            print(f'Sorry, there is not enough {a}.')

        else:
            print('Please insert coins!')
            m1, m2, m3, m4 = int(input('how many quarters?: ')), int(input('how many dimes?: ')), int(
                input('how many nickles?: ')), int(input('how many pennies?: '))
            m_total = m1 * 25 + m2 * 10 + m3 * 5 + m4

            if m_total < MENU[select_product]['cost'] * 100:
                print("Sorry, that´s not enough money. Money refunded.")

            else:
                if m_total == MENU[select_product]['cost'] * 100:
                    print(f"Here is your {select_product}. Enjoy")

                else:
                    print(f"Here is {(MENU[select_product]['cost'] * 100 - m_total) / -100} in change.")
                    print(f"Here is your {select_product}. Enjoy.")

                money_total += MENU[select_product]['cost']
                for i in ingr_of_select_product:
                    left_resources[i] -= ingr_of_select_product[i]




    else:
        print(f"Water: {left_resources['water']}ml.")
        print(f"Milk: {left_resources['milk']}ml.")
        print(f"Coffee: {left_resources['coffee']}g.")
        print(f'Money: ${money_total}')
