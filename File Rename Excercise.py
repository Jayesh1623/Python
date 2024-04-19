import os

# print(dir(os))

# os.rename("TempFolder/Text1.txt", "TempFolder/String1")

files = os.listdir("TempFolder")
i=1
for file in files:
    if file.endswith(".png"):
         os.rename(f"TempFolder/{file}", f"TempFolder/Img{i}.png")
         i=i+1