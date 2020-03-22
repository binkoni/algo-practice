local N = io.read()
local numbers = io.read()
local sum = 0
for number in string.gmatch(numbers, "(%d)") do
    sum = sum + number
    --print(number)
end
print(math.floor(sum))
