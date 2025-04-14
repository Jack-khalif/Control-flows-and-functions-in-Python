# Function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    #  Calculate final price using the function
    final_price = calculate_discount(original_price, discount_percentage)

    #  Display the final result
    if final_price != original_price:
        print(f"Final price after {discount_percentage}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The final price is: {original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
