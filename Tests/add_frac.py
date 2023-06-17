def number_from_other_side(n):
    k = 1 
    a = 1 
    length = 0
    sum_next_numbers = 0
    while n // a != 0:
        length += 1 
        a = a * 10
    length -= 1
    number_1 = n // (10**(length))
    if length == 0:
        return number_1
    while length - k > 0:
        next_number_1 = n // 10**(length - k) 
        next_number_2 = ( next_number_1 - 10**k * (next_number_1 // 10) ) * 10**k
        sum_next_numbers += next_number_2     
        k += 1
    last_number = (n - (n // 10) * 10) * 10**length
    reverse_number = sum_next_numbers + number_1 + last_number
   
    return reverse_number

print(number_from_other_side(3))