
def calculate_discount(price, discount_rate, quantity):
    """Calculate subtotal, discount amount, and final total."""

    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount_rate <= 100:
        raise ValueError("Discount rate must be between 0 and 100.")

    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    subtotal = price * quantity
    discount_amount = subtotal * discount_rate / 100
    final_total = subtotal - discount_amount

    return {
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "final_total": final_total,
    }
