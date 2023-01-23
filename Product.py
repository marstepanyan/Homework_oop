class Product:
    def __init__(self, name, price, product_id, description):
        self._name = name
        self._price = price
        self._description = description
        self._product_it = product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description

    def get_product_id(self):
        return self._product_it

    def set_name(self, new_name):
        self._name = new_name

    def set_price(self, new_price):
        self._price = new_price

    def set_description(self, new_description):
        self._description = new_description

    def __repr__(self):
        return str(dict(name=self._name, price=self._price, product_id=self._product_it, description=self._description))
