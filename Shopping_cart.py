class ShoppingCart:
    def __init__(self, user):
        self._cart = []
        self._user_id = user._user_id

    def get_cart(self):
        return self._cart

    def get_user_id(self):
        return self._user_id

    def add_to_cart(self, added_product):
        self._cart.append(added_product)

    def remove_from_cart(self, removed_product):
        self._cart.remove(removed_product)

    def get_total_price(self):
        total = 0
        for item in self._cart:
            total += item.get_price()

        return total
