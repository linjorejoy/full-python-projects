import torch

print("\nInitial Reshaping")
tensor_1 = torch.arange(12)
print(f"{tensor_1 = }")

tensor_1_3x3_1 = tensor_1.view(3, 4)  # faster if used properly but can cause error if array is not contiguous
tensor_1_3x3_2 = tensor_1.reshape(3, 4)  # safer

print(f"{tensor_1_3x3_1 = }")
print(f"{tensor_1_3x3_2 = }")

print("\nConcat")
tensor_2 = torch.rand((2, 5))
tensor_3 = torch.rand((2, 5))

print(f"{tensor_2 = }")
print(f"{tensor_3 = }")
print(f"{torch.cat((tensor_2, tensor_3), dim=0) = }")
print(f"{torch.cat((tensor_2, tensor_3), dim=1) = }")

print("\nTranspose")
print(f"{tensor_2.t() = }")

print("\nFlatten")

print(tensor_2.view(-1))

batch = 64
tensor_4 = torch.rand((batch, 2, 5))
print(tensor_4.view(batch, -1).shape)
print(tensor_4.view(-1, 10).shape)

print("\nShifting Dimensions")
tensor_5 = tensor_4.permute(0, 2, 1)
print(tensor_5.shape)

print("\nUn-squeeze")
tensor_6 = torch.arange(10)
print(f"{tensor_6 = }")
print(f"{tensor_6.unsqueeze(0) = }")
print(f"{tensor_6.unsqueeze(1) = }")
print(f"{tensor_6.unsqueeze(0).unsqueeze(1) = }")
print(f"{tensor_6.unsqueeze(1).unsqueeze(0) = }")
