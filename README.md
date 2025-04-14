Absolutely — here’s a clean, simple, and professional `README.md` for your discount calculator project:

---

# 📦 Discount Calculator

## 📖 Description
This is a simple Python program that calculates the final price of an item after applying a discount. It uses a function named `calculate_discount(price, discount_percent)` which checks whether the given discount is **20% or higher**:
- If the discount is **20% or more**, it applies the discount to the original price.
- If the discount is **less than 20%**, the original price is returned without any changes.

The program interacts with the user by:
- Prompting for the original price of the item.
- Prompting for the discount percentage.
- Displaying the final price after applying the discount (if applicable).

---

## 🛠️ Features
- 📉 Calculates discounts only if **20% or higher**.
- 🎛️ Takes user input for both price and discount percentage.
- 🛑 Includes input validation for numeric entries.
- 📊 Displays the final price after applying the discount or confirms no discount applied.

---

## How to Use

1. **Run the program** using Python:
   ```bash
   flows.py
   ```

2. **Enter the original price** of the item when prompted.

3. **Enter the discount percentage** when prompted.

4. **View the final price**:
   - If discount ≥ 20%, it shows the discounted price.
   - If discount < 20%, it confirms no discount applied and displays the original price.

---

##  Example

```
Enter the original price of the item: 500
Enter the discount percentage: 25
Final price after 25.0% discount is: 375.00
```

```
Enter the original price of the item: 500
Enter the discount percentage: 10
No discount applied. The final price is: 500.00
```

---

## Requirements
- Python 3.x

---

##  License
This project is open for educational and learning purposes.

