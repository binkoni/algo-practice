local numbers = {}
for i = 1, 3 do
    table.insert(numbers, io.read("*n"))
end
table.sort(numbers, function(a, b) return a > b end)

print(numbers[2])
