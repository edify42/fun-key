# The Base58 digits
base58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(address_bignum):
    """This function converts a big int as a string to a
    base58 encoded string.
    :returns: The string in base58
    """
    b58_string = ""
    # Get the number of leading zeros
    leading_zeros = len(address_bignum) - len(address_bignum.lstrip('0'))
    # Convert hex to decimal
    address_int = int(address_bignum, 10)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = base58_digits[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add ‘1’ for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = '1' + b58_string
    return b58_string
 
def base58_decode(address):
    """This function converts an base58 string to a numeric
    format.
 
    :param address: The base58 string
    :returns: The numeric value decoded
    """
    address_bignum = 0
    for char in address:
        address_bignum *= 58
        digit = base58_digits.index(char)
        address_bignum += digit
    return address_bignum