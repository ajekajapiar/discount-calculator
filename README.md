
# Discount Calculator

A simple Python program that calculates the final price
of items after applying a discount.

## Features

- Calculate subtotal based on price and quantity
- Apply percentage-based discounts
- Display the discount amount and final total
- Show savings in Indonesian Rupiah (IDR)
- Validate user input
- Include unit tests using Python's unittest module

## Requirements

- Python 3.9 or newer
- No external dependencies required

## Project Structure

```text
discount-calculator/
├── main.py
├── calculator.py
├── test_calculator.py
├── README.md
└── .gitignore
```

## How to Run

1. Clone this repository.
2. Open the project folder in your terminal.
3. Run the program:

```bash
python main.py
```

## Example

Input:
- Price per item: Rp100,000
- Discount rate: 20%
- Quantity: 3

Output:
- Subtotal: Rp300,000.00
- Discount: Rp60,000.00
- Final total: Rp240,000.00
- Savings: Rp60,000.00

## Run Tests

```bash
python -m unittest -v
```

## Author

Azka Zaviar
