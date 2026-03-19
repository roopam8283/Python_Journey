

#  Mutable and Immutable objects

sugar_amount = 100
print(f"initial sugar amount: {sugar_amount}")
secondary_sugar_amount = 200
print(f"secondary sugar amount is {secondary_sugar_amount}")

print(id(sugar_amount))
print(id(secondary_sugar_amount))

# To check the objec is mutable or not , check the id of the object before and after the change