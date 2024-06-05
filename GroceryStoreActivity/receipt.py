import csv

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
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    products_dict = read_dictionary('GroceryStoreActivity/products.csv', 0)
    
    print(products_dict)
    
    with open('GroceryStoreActivity/request.csv', mode='r') as file:
        reader = csv.reader(file)
        
        next(reader) 
        
        for row in reader:
            product_number = row[0]
            requested_quantity = int(row[1])
            
            product_info = products_dict[product_number]
            product_name = product_info[1]
            product_price = float(product_info[2])
            
            print(f'Product: {product_name}, Quantity: {requested_quantity}, Price: {product_price}')

if __name__ == "__main__":
    main()
