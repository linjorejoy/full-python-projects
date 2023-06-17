import torch
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"
# device = "cpu"

tensor_1 = torch.tensor([[1, 2, 3], [3, 5, 8]], dtype=torch.float16, device=device)
print(tensor_1)
print(tensor_1.device)
print(tensor_1.dtype)
print(tensor_1.shape)
row, col = tensor_1.shape
print(row, col)
print(tensor_1.requires_grad)

# Other ways of initialization

tensor_2 = torch.empty(size=(3, 5))
tensor_3 = torch.zeros(size=(3, 5))
tensor_4 = torch.rand((3, 5))
tensor_5 = torch.ones(size=(3, 5))
tensor_6 = torch.eye(5, 5)  # Identity Matrix
tensor_7 = torch.arange(start=0, end=10, step=2)
tensor_8 = torch.linspace(start=0, end=2, steps=8)
tensor_9 = torch.empty(size=(3, 5)).normal_(mean=0, std=1)
tensor_10 = torch.empty(size=(3, 5)).uniform_(0, 1)
tensor_11 = torch.diag(torch.ones(5))

print(f"{tensor_2 = }")
print(f"{tensor_3 = }")
print(f"{tensor_4 = }")
print(f"{tensor_5 = }")
print(f"{tensor_6 = }")
print(f"{tensor_7 = }")
print(f"{tensor_8 = }")
print(f"{tensor_9 = }")
print(f"{tensor_10 = }")
print(f"{tensor_11 = }")

# Converting to different types

tensor_12 = torch.arange(10)

print(f"{tensor_12.bool() = } ===> {tensor_12.bool().dtype = }")
print(f"{tensor_12.short() = } ===> {tensor_12.short().dtype = }")
print(f"{tensor_12.long() = } ===> {tensor_12.long().dtype = }")
print(f"{tensor_12.half() = } ===> {tensor_12.half().dtype = }")
print(f"{tensor_12.float() = } ===> {tensor_12.float().dtype = }")
print(f"{tensor_12.double() = } ===> {tensor_12.double().dtype = }")


# numpy -> tensors -> numpy
np_array_1 = np.zeros((5, 5))
tensor_13 = torch.from_numpy(np_array_1)
np_array_1_1 = tensor_13.numpy()

print(f"{tensor_13 = }  ===> {tensor_13.dtype = }")
print(f"{np_array_1_1 = }")


