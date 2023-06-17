import torch

print("\nINITIAL VALUES")

tensor_1 = torch.tensor([1, 2, 3])
tensor_2 = torch.tensor([9, 8, 7])

print(f"{tensor_1 = } ===> {tensor_1.dtype}")
print(f"{tensor_2 = } ===> {tensor_2.dtype}")

# Addition
print("\nADDITION")
sum_tensor_1 = torch.empty(3)
torch.add(tensor_1, tensor_2, out=sum_tensor_1)

sum_tensor_2 = torch.add(tensor_1, tensor_2)

sum_tensor_3 = tensor_1 + tensor_2

print(f"{sum_tensor_1 = } ===> {sum_tensor_1.dtype = }")
print(f"{sum_tensor_2 = } ===> {sum_tensor_2.dtype = }")
print(f"{sum_tensor_3 = } ===> {sum_tensor_3.dtype = }")

# Subtraction
print("\nSUBTRACTION")
sub_tensor_1 = torch.empty(3)
torch.subtract(tensor_1, tensor_2, out=sub_tensor_1)

sub_tensor_2 = torch.subtract(tensor_1, tensor_2)

sub_tensor_3 = tensor_1 - tensor_2

print(f"{sub_tensor_1 = } ===> {sub_tensor_1.dtype = }")
print(f"{sub_tensor_2 = } ===> {sub_tensor_2.dtype = }")
print(f"{sub_tensor_3 = } ===> {sub_tensor_3.dtype = }")

# Division
print("\nDIVISION")
div_tensor_1 = torch.true_divide(tensor_1, tensor_2)
div_tensor_2 = tensor_1 / tensor_2

print(f"{div_tensor_1 = } ===> {div_tensor_1.dtype = }")
print(f"{div_tensor_2 = } ===> {div_tensor_2.dtype = }")
print(f"{tensor_1/2 = } ===> {(tensor_1/2).dtype = }")

# Inplace Operations
print("\nINPLACE OPERATIONS")

inplace_1 = torch.zeros(3)

# add_ : anything which is ending with _ is inplace
inplace_1.add_(tensor_1)
print(f"{inplace_1 = } ===> {inplace_1.dtype = }")

# += is also inplace but tensor_3 = tensor_3 + tensor_2 is not inplace
inplace_1 += tensor_2
print(f"{inplace_1 = } ===> {inplace_1.dtype = }")

print("\nEXPONENTIATION")

expo_1 = tensor_1.pow(2)

expo_2 = tensor_1 ** 2

print(f"{expo_1 = } ===> {expo_1.dtype = }")
print(f"{expo_2 = } ===> {expo_2.dtype = }")

print("\nCOMPARISONS")

print(f"{tensor_1 = } ===> {tensor_1.dtype}")
compare_1 = tensor_1 > 2
print(f"tensor_1 > 2 : {compare_1 = } ===> {compare_1.dtype = }")
compare_1 = tensor_1 < 2
print(f"tensor_1 < 2 : {compare_1 = } ===> {compare_1.dtype = }")
compare_1 = tensor_1 <= 2
print(f"tensor_1 <= 2 : {compare_1 = } ===> {compare_1.dtype = }")
compare_1 = tensor_1 >= 2
print(f"tensor_1 >= 2 : {compare_1 = } ===> {compare_1.dtype = }")
compare_1 = tensor_1 == 2
print(f"tensor_1 == 2 : {compare_1 = } ===> {compare_1.dtype = }")
compare_1 = tensor_1 != 2
print(f"tensor_1 != 2 : {compare_1 = } ===> {compare_1.dtype = }")

print("\nMATRIX MULTIPLICATION")
tensor_7 = torch.rand((2, 3))
tensor_8 = torch.rand((3, 5))

mat_mul_1 = torch.mm(tensor_7, tensor_8)
mat_mul_2 = tensor_7.mm(tensor_8)

print(f"{mat_mul_1 = } ===> {mat_mul_1.dtype = }")
print(f"{mat_mul_2 = } ===> {mat_mul_2.dtype = }")

print("\nMATRIX EXPONENTIATION")
tensor_9 = torch.rand((3, 3))

print(tensor_9)
mat_exp_1 = tensor_9.mm(tensor_9).mm(tensor_9)
mat_exp_2 = tensor_9.matrix_power(3)

print(f"{mat_exp_1 = } ===> {mat_exp_1.dtype = }")
print(f"{mat_exp_2 = } ===> {mat_exp_2.dtype = }")

print("\nELEMENT WISE MULTIPLICATION")

ele_wise_mul_1 = tensor_1 * tensor_2

print(f"{ele_wise_mul_1 = } ===> {ele_wise_mul_1.dtype = }")

print("\nDOT PRODUCT")

dot_prod_1 = torch.dot(tensor_1, tensor_2)
print(f"{dot_prod_1 = } ===> {dot_prod_1.dtype = }")

print("\nBATCH MATRIX MULTIPLICATION")
batch = 32
n = 10
m = 20
p = 30
tensor_10 = torch.rand((batch, n, m))
tensor_11 = torch.rand((batch, m, p))
out_bmm = torch.bmm(tensor_10, tensor_11)  # Will be shape: (b x n x p)
print(f"{out_bmm = }")

print("\nBROADCASTING")

tensor_12 = torch.rand((5, 5))
tensor_13 = torch.rand((1, 5))

# Here tensor_13 will be expanded to match the size of tensor_12
broadcast_result_1 = tensor_12 - tensor_13
broadcast_result_2 = tensor_12 ** tensor_13
broadcast_result_3 = tensor_12 * tensor_13

print(f"{broadcast_result_1 = } ===> {broadcast_result_1.dtype = }")
print(f"{broadcast_result_2 = } ===> {broadcast_result_2.dtype = }")
print(f"{broadcast_result_3 = } ===> {broadcast_result_3.dtype = }")

print("\nOTHER USEFUL TENSOR OPERATIONS")

tensor_14 = torch.rand((3, 5))
sum_x_1 = torch.sum(tensor_14, dim=0)
sum_x_2 = torch.sum(tensor_14, dim=1)

print(f"{tensor_14 = } ===> {tensor_14.dtype = }")
print(f"{sum_x_1 = } ===> {sum_x_1.dtype = }")
print(f"{sum_x_2 = } ===> {sum_x_2.dtype = }")

values_max_1, indices_max_1 = torch.max(tensor_14, dim=0)
values_max_2, indices_max_2 = torch.max(tensor_14, dim=1)
max_indices = torch.argmax(tensor_14, dim=0)

values_min_1, indices_min_1 = torch.min(tensor_14, dim=0)
values_min_2, indices_min_2 = torch.min(tensor_14, dim=1)
min_indices = torch.argmin(tensor_14, dim=0)

print(f"{values_max_1 = } ===> {indices_max_1 = }")
print(f"{max_indices = } ===> {max_indices = }")
print(f"{values_max_2 = } ===> {indices_max_2 = }")

print(f"{values_min_1 = } ===> {indices_min_1 = }")
print(f"{min_indices = } ===> {min_indices = }")
print(f"{values_min_2 = } ===> {indices_min_2 = }")

abs_1 = torch.abs(tensor_14)
print(f"{abs_1 = } ===> {abs_1.dtype = }")
print(f"{torch.mean(tensor_14.float(), dim=0) = } ===> {torch.mean(tensor_14.float(), dim=0) = }")

print("\n\n")
tensor_15 = torch.eye(5, 5)
tensor_16 = torch.ones((5, 5))

print(f"{tensor_15 = }")
print(f"{tensor_16 = }")

print(f"{torch.eq(tensor_15, tensor_16) = }")
print(f"{torch.lt(tensor_15, tensor_16) = }")
print(f"{torch.eq(tensor_15, tensor_16) = }")

print("\n\n")
print(f"{tensor_1 = }")
print(f"{torch.sort(tensor_1, dim=0, descending=True) = }")

tensor_17 = torch.tensor([9, 8, 7, 5, 12, 15, 8, 6, -2, 1, 0, -5, 20])
clamp_tensor_1 = torch.clamp(tensor_17, min=0, max=10)

print(f"{tensor_17 = }")
print(f"{clamp_tensor_1 = }")

tensor_18 = torch.tensor([1, 0, 1, 1], dtype=torch.bool)
print(f"{torch.any(tensor_18) = }")
print(f"{torch.all(tensor_18) = }")

