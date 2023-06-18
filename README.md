# zag

## Introduction
This Python program is designed to update product price and inventory information. when execute the function, It will get product id(item code) from zag_shop.zag_prodoct_control to fetch the product information in Rakuten API every 0.25s. 

## Requirements
To run this program, you need the following dependencies:
- Python [>= 3.6]
- requests
- mysql-python-connect

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using the following command:
   ```
   python -m pip install -r requirements.txt
   ```

## Usage
1. Execute the command
    ```
    python function.py
    ```
2. The following result will be output.
- `[number] recodes will be inserted rakutencon.zag_product_inventory_history` - execute successfully.
- `[429]` - from Rakuten API, It means request too many times in a short time.
- `insert error [message]` - when insert database, there is error

## Configuration
no Configuration

## File Structure
- `function.py`: the function entrance.
- `conn_db.py`: config the mysql database.
- `rakutenAPI.py`: Rankuten API defination.
- `output/`: [Description of the directory structure and purpose of any output files].

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please submit a pull request. 

## Contact
If you have any questions or feedback, feel free to contact Haku at baichuqi@gmail.com.

## Acknowledgements
- CRUD in mysql DB
- Scraping data from Rakuten API

---
Feel free to customize the sections and provide more specific details based on your Python program.