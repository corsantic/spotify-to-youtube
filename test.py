#%%
import io

with open("secret.txt", "r") as f:
    lines = f.readlines()

#%%
q = lines[lineIndex]
result = q.split(splitStr)[splitIndex].strip()

