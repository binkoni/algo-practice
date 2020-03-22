local score = io.read("*n")
if 90 <= score and score <= 100 then
    print("A")
elseif 80 <= score and score <= 89 then
    print("B")
elseif 70 <= score and score <= 79 then
    print("C")
elseif 60 <= score and score <= 69 then
    print("D")
else
    print("F")
end
