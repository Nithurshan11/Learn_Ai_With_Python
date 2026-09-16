"""
Input a product code, name and price.
Using a function, write product details to a text file.
Use another function to read the text file
and display the product details.
"""


# Function to write product details
def write_prod_data(code, name, price):

    fp = open("prod.txt", "w")

    fp.write(
        f"Product Code : {code}\n"
        f"Product Name : {name}\n"
        f"Product Price : {price}\n"
    )

    fp.close()

"""
def read_prod_data():
    whit open("prod.txt", "r") as fp:
        for prod_data in fp:
              print(prod_data.strip())
     fp.close()

"""


# Function to read product details
def read_prod_data():

    fp = open("prod.txt", "r")

    for prod_data in fp:
        print(prod_data.strip())

    fp.close()


# Main program
p_code = input("Enter Product Code: ")
p_name = input("Enter Product Name: ")
p_price = float(input("Enter Product Price: "))

write_prod_data(p_code, p_name, p_price)

print("\nProduct Details from the File")

read_prod_data()
