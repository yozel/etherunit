# etherunit
Etherium unit conversation and arithmetic library

## Install
```sh
pip install -u etherunit
```

## Usage

```python
>>> from etherunit import Ether, Gwei, Wei, E
```
### Create a new quantity with units
You can create a new quatity like this
```python
>>> Ether(".05")
0.05 ether
>>> Gwei(".05")
0.05 gwei
>>> Wei("5")
5 wei
```
Or you can use the helper function E() to create a new quantity
```python
>>> E(".05 eth")
0.05 ether
>>> E(".05 gwei")
0.05 gwei
>>> E("5 wei")
5 wei
```
### Arithmetic operations
Different quatities can be added together without any problems
```python
>>> E(".05 eth") + E("2 gwei") == E("0.050000002 eth")
True
```
This also applies for subtraction
```python
>>> E(".05 eth") - E("2 gwei") == E("0.049999998 eth")
True
```
You can also multiply quanities with other integers
```python
>>> E(".05 eth") * 2
0.1 ether
```
... but not with other quatities
```python
>>> E(".05 eth") * E("2 gwei")  # type: ignore
AssertionError: 2 gwei is not an integer
```
You also can't multiply quatities with other integers, like floats. Why? Because it can result with fractional wei, which is not allowed
```python
>>> E(".05 eth") * 1.5
AssertionError: 1.5 is not an integer
```
You can divide quatities with other integers, the result is always a quatity
```python
>>> E(".05 eth") / 2
0.025 ether
```
And you can divide quatities with other quatities, the result is always an integer
```python
>>> E("10 eth") / E("3 eth")
3
```
You can find the remainder of a division with mod operator (%)
```python
>>> E("10 eth") % E("3 eth")
1 ether
```
You can also use divmod() to get both the quotient and the remainder
```python
>>> divmod(E("10 eth"), E("3 eth"))
(3, 1 ether)
```

### Conversion
You can convert a quatity to another quatity, though it's not necessary for arithmetic operations
```python
>>> E("10 eth").gwei
10000000000 gwei
>>> E("10 eth").wei
10000000000000000000 wei
>>> (E("10 eth") % E("3 eth")).wei
1000000000000000000 wei
>>> E("10 eth").wei.eth.eth.eth.eth.gwei.wei.wei.wei  # :D
10000000000000000000 wei
```

