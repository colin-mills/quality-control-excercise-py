import csv
import os

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
csv_headers = ["id", "name", "aisle", "department", "price"]


def read_from_csv(my_csv_filepath):

    products = []

    with open(my_csv_filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))
    return products

def write_to_file(my_products, my_filepath):
        with open(my_filepath, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()

        for product in my_products:
            writer.writerow(product)



def autogen_id(products):
    ID = len(products) + 1
    return ID
#
# READ
#

#Only runs if script is run from command line
if __name__ == "__main__":

    products = read_from_csv(csv_filepath)

    #with open(csv_filepath, "r") as csv_file:
    #    reader = csv.DictReader(csv_file)
    #    for ordered_dict in reader:
    #        products.append(dict(ordered_dict))

    #
    # LIST
    #

    print("---------------------")
    print("LISTING PRODUCTS:")

    for product in products:
        print(f"  {product['id']}) {product['name']} ")

    #
    # CREATE
    #

    print("---------------------")
    print("CREATING A NEW PRODUCT:")

    new_product = {
        "name": "My New Product",
        "aisle": "Some Aisle",
        "department": "Some Department",
        "price": 99.99
    } # further exploration / todo: ask for user to input

    next_id = len(products) + 1

    new_product["id"] = next_id

    print(new_product)

    products.append(new_product)

    #
    # WRITE
    #

    write_to_file(products, csv_filepath)
    #with open(csv_filepath, "w") as csv_file:
    #    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    #    writer.writeheader()
#
    #    for product in products:
    #        writer.writerow(product)
