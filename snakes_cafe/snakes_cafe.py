menu = '''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
'''

order_prompt = '''***********************************
** What would you like to order? **
***********************************
'''
print(menu)
print(order_prompt)

order_items = []
order = 0
item = str(input('> '))

while item != 'quit':
  if item.capitalize() == 'Wings':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Cookies':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Spring Rolls':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Salmon':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Steak':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Meat Tornado':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'A Literal Garden':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Ice Cream':
    print(f'** 1 order of {item} have been added to your meal')
  elif item.capitalize() == 'Cake':
    print(f'** 1 order of {item} have been added to your meal')
  else :
    print('** Please enter a valid menu item, Thank you **')    
  order_items.append(item)
  item = str(input('> '))
print('Thank you for your order, you have ordered the items below')
print(' '.join(order_items))