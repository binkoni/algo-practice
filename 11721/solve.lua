local input = io.read()
local count = 0
for character in string.gmatch(input, ".") do
    io.write(character)
    count = count + 1
    if count % 10 == 0 then
        print()
    end
end
