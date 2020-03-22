--lua 5.3

local N = io.read("*n")
--print("N: " .. N)
local bag5Count = math.floor(N / 5)
local bag3Count = 0
while bag5Count >= 0 do
    bag3Count = math.floor((N - 5 * bag5Count) / 3)
    while bag3Count >= 0 do
        --print("bag5Count: " .. bag5Count .. ", bag3Count: " .. bag3Count)
        if N - 5 * bag5Count - 3 * bag3Count == 0 then
            goto success
        end
        bag3Count = bag3Count - 1
    end
    bag5Count = bag5Count - 1
end

print(-1) --failure
os.exit()

::success:: --success

print(bag5Count + bag3Count)