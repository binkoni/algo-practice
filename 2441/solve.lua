local n = io.read("*n")
for i = 1, n do
    for j = 1, i - 1 do
        io.write(" ")
    end
    for j = 1, n - i + 1 do
        io.write("*")
    end
    io.write("\n")
end
