import User
import Shopping_cart
import Product

harry = User.User('harry_potter', 'harrypotter@email', 'a0001')
harry_shopping_cart = Shopping_cart.ShoppingCart(harry)

# print(harry_shopping_cart.get_user_id())

pr = Product.Product('sofa', 350000, 's345', {'color': 'pink', 'shape': 'S'})
print("product sofa: ", pr)


pr1 = Product.Product('table', 50000, 's305', {'color': 'black', 'shape': 'triangle'})
print("product table: ", pr1)

harry_shopping_cart.add_to_cart(pr)
harry_shopping_cart.add_to_cart(pr1)

print('cart: ', harry_shopping_cart.get_cart())
print('total price: ', harry_shopping_cart.get_total_price())
