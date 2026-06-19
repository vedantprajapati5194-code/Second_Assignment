# Que_3:- Build a list of tuples using list comprehension where each tuple contains a Flipkart product name and its price, but only include products with prices above 1000 from the given lists: names = ['Shoes', 'Bag', 'Watch', 'Headphones'], prices = [999, 1500, 700, 2200].

names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

products = [(name, price) for name, price in zip(names, prices) if price > 1000]

print(products)