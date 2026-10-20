
from calculator import calculate_discount


def format_rupiah(amount):
    """Format a number as Indonesian Rupiah."""
    formatted = f"{amount:,.2f}"
    formatted = formatted.replace(",", "TEMP").replace(".", ",")
    formatted = formatted.replace("TEMP", ".")
    return f"Rp{formatted}"


def get_positive_price():
    while True:
        try:
            price = float(input("Enter price per item (Rp): "))
            if price < 0:
                print("Error: Price cannot be negative.")
                continue
            return price
        except ValueError:
            print("Error: Please enter a valid number.")


def get_discount_rate():
    while True:
        try:
            rate = float(input("Enter discount rate (%): "))
            if not 0 <= rate <= 100:
                print("Error: Discount must be between 0 and 100.")
                continue
            return rate
        except ValueError:
            print("Error: Please enter a valid number.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
            return quantity
        except ValueError:
            print("Error: Quantity must be a whole number.")


def main():
    print("=" * 40)
    print("       DISCOUNT CALCULATOR")
    print("=" * 40)

    price = get_positive_price()
    discount_rate = get_discount_rate()
    quantity = get_quantity()

    result = calculate_discount(price, discount_rate, quantity)

    print("\n" + "=" * 40)
    print("          PAYMENT SUMMARY")
    print("=" * 40)
    print(f"Price per item : {format_rupiah(price)}")
    print(f"Quantity       : {quantity}")
    print(f"Subtotal       : {format_rupiah(result['subtotal'])}")
    print(f"Discount ({discount_rate:g}%) : -{format_rupiah(result['discount_amount'])}")
    print("-" * 40)
    print(f"FINAL TOTAL    : {format_rupiah(result['final_total'])}")
    print(f"You saved      : {format_rupiah(result['discount_amount'])}")
    print("=" * 40)


if __name__ == "__main__":
    main()
