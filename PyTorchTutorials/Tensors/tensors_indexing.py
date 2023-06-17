import torch

batch_size = 10
features = 5

tensor_1 = torch.rand((batch_size, features))

print(f"{tensor_1} ==> {tensor_1.shape}")
print("\nFirst Dim")
print(f"{tensor_1[0] = } ==> {tensor_1[0].shape}")
print(f"{tensor_1[0, :] = } ==> {tensor_1[0, :].shape}")
print(f"{tensor_1[0][0]} ==> {tensor_1[0][0].shape}")

print("\nFirst of all Dim")
print(f"{tensor_1[:, 0] = } ==> {tensor_1[:, 0].shape}")

print("\nFirst n features of mth batch")
m = 2
n = 4
print(f"{tensor_1[m, 0:n] = } ==> {tensor_1[m, 0:n].shape}")

print("\nRemove Border elements")

row, col = tensor_1.shape
print(f"{tensor_1[1:row-1, 1:col-1] = } ==> {tensor_1[1:row - 1, 1:col - 1].shape}")

print("\nFancy Indexing")
tensor_2 = torch.arange(10)
indices = [2, 4, 8]

print(f"{tensor_2 = }")
print(f"{tensor_2[indices] = }")

print("\nSpecial Indexing")
tensor_3 = torch.rand((3, 5))
print(f"tensor_3 =\n{tensor_3}")

rows_1 = torch.tensor([1, 0])
cols_1 = torch.tensor([4, 0])
print(f"{rows_1 = }")
print(f"{cols_1 = }")
print(f"{tensor_3[rows_1, cols_1] = }")

rows_2 = torch.tensor([1, 1])
cols_2 = torch.tensor([4, 1])
print(f"{rows_2 = }")
print(f"{cols_2 = }")
print(f"{tensor_3[rows_2, cols_2] = }")

rows_2 = torch.tensor([1, 2])
cols_2 = torch.tensor([4, 2])
print(f"{rows_2 = }")
print(f"{cols_2 = }")
print(f"{tensor_3[rows_2, cols_2] = }")

print("\nMORE ADVANCED INDEXING")

tensor_4 = torch.arange(10)
print(f"{tensor_4 = }")
print(f"{tensor_4[(tensor_4 < 2)] = }")
print(f"{tensor_4[(tensor_4 > 8)] = }")
print(f"{tensor_4[(tensor_4 < 2) | (tensor_4 > 8)] = }")
print(f"{tensor_4[(tensor_4 > 2) & (tensor_4 < 8)] = }")
print(f"{tensor_4[(tensor_4.remainder(2) == 0)] = }")
print(f"{tensor_4[(tensor_4 % 2 == 0)] = }")

print("\nUseful Operations")
print(f"{tensor_4 = }")
print(torch.where(tensor_4 > 5, tensor_4, tensor_4 * 2))

print(f"{torch.tensor([0, 1, 0, 2, 2, 3, 4, 8, 5, 7]).unique() = }")
print(f"{torch.tensor([0, 1, 0, 2, 2, 3, 4, 8, 5, 7]).unique(sorted=False) = }")
print(tensor_4.ndimension())  # Num of Dimensions
print(tensor_4.numel())  # Num of Elements
