from etherunit import Ether, Gwei, Wei, E

# Create a new quantity with units

## You can create a new quatity like this
Ether(".05")
Gwei(".05")
Wei("5")

## Or you can use the helper function E() to create a new quantity
E(".05 eth")
E(".05 gwei")
E("5 wei")

# Arithmetic operations

## Different quatities can be added together without any problems
E(".05 eth") + E("2 gwei") == E("0.050000002 eth")

## This also applies for subtraction
E(".05 eth") - E("2 gwei") == E("0.049999998 eth")

## You can also multiply quanities with other integers
E(".05 eth") * 2

## ... but not with other quatities
try:
    E(".05 eth") * E("2 gwei")  # type: ignore
except AssertionError as e:
    print("Error:", e)

## You also can't multiply quatities with other integers, like floats
## Why? Because it can result with fractional wei, which is not allowed
try:
    E(".05 eth") * 1.5  # type: ignore
except AssertionError as e:
    print("Error:", e)

## You can divide quatities with other integers, the result is always a quatity
E(".05 eth") / 2

## And you can divide quatities with other quatities, the result is always an integer
E("10 eth") / E("3 eth")

## You can find the remainder of a division with mod operator (%)
E("10 eth") % E("3 eth")

## You can also use divmod() to get both the quotient and the remainder
divmod(E("10 eth"), E("3 eth"))

# Conversion
## You can convert a quatity to another quatity, though it's not necessary for arithmetic operations
E("10 eth").gwei
E("10 eth").wei
(E("10 eth") % E("3 eth")).wei
E("10 eth").wei.eth.eth.eth.eth.gwei.wei.wei.wei  # :D
