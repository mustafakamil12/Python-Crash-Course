#import pizza_module

#pizza_module.make_pizza(16, 'pepperoni')
#pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#from pizza_module import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#from pizza_module import make_pizza as mp

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')


import pizza_module  as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
