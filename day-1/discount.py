n1=float(input("Enter the original price: "))
n2=float(input("Enter the discount percentage: "))
discount_amount=(n1*n2)/100 #Calculate the discount amount by multiplying the original price (n1) with the discount percentage (n2) and dividing by 100 to get the actual discount value.
final_price=n1-discount_amount
print("The discount amount is: ",discount_amount)
print("The final price after discount is: ",final_price)
