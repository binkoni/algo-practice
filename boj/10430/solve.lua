local A = io.read("*n")
local B = io.read("*n")
local C = io.read("*n")
print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)
