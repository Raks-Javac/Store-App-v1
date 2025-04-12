from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
            print("Call cart endpoint:")
            response = self.client.post('/store/carts/')
            print("Cart creation status:", response.status_code)
            print("Cart creation body:", response.text)
            if response.status_code == 201 or response.status_code == 200:
                self.cart_id = response.json()['id']
            else:
                self.cart_id = None
            self.add_to_cart()
            return super().on_start()


    @task(2)
    def view_products(self):
        print("View products")
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}',
            name='/store/products'
        )

    @task(4)
    def view_product(self):
        print("View product details")
        product_id = randint(1, 20)  # Adjust based on actual DB
        self.client.get(
            f'/store/products/{product_id}',
            name='/store/products/[id]'
        )

    
    def add_to_cart(self):
        print('Add to Cart')
        product_id = randint(1,10)  # <-- Might pick an ID that doesn't exist
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items', 
            json={'product_id': product_id, 'quantity': 1}
        )
    
    @task
    def say_hello(self):
         self.client.get('/playground/hello/')
         

