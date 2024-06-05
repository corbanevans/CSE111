import csv
import os
import random
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
    return dictionary

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        
        
        
        request_file_path = 'request.csv'
        if not os.path.isfile(request_file_path):
            print(f"Error: The file {request_file_path} does not exist.")
            return
        
        with open(request_file_path, mode='r') as file:
            reader = csv.reader(file)
            
            
            next(reader)  
            
            print("Inkom Emporium")
            total_items = 0
            subtotal = 0.0
            ordered_products = []
            
            for row in reader:
                product_number = row[0]
                requested_quantity = int(row[1])
                
                
                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    
                    
                    print(f'{product_name}: {requested_quantity} @ {product_price:.2f}')
                    
                    total_items += requested_quantity
                    subtotal += requested_quantity * product_price

                    ordered_products.append((product_name, product_price))
                else:
                    raise KeyError(f"Error: Product number {product_number} not found in products dictionary.")
            
            
            sales_tax_rate = 0.06
            sales_tax = subtotal * sales_tax_rate
            total_due = subtotal + sales_tax
            
            print(f'Number of Items: {total_items}')
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {sales_tax:.2f}')
            print(f'Total: {total_due:.2f}')
            print("Thank you for shopping at the Inkom Emporium.")
            
            current_date_and_time = datetime.now()
            print(f'{current_date_and_time:%a %b %d %H:%M:%S %Y}')

            if ordered_products:
                coupon_product = random.choice(ordered_products)
                coupon_product_name, coupon_product_price = coupon_product
                discount_amount = coupon_product_price * 0.10  # Example: 10% discount
                print(f"\nCoupon: Get 10% off your next purchase of {coupon_product_name}!")
                print(f"Save ${discount_amount:.2f} on your next purchase.")
    
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()
