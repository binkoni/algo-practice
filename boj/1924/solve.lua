local targetMonth, targetMDay = io.read("*n"), io.read("*n")
local mLastDays = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
local wDays = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"}
local wDayIndex = 1
local currentMonth, currentMDay = 1, 1

while currentMonth < targetMonth or currentMDay < targetMDay do
    --print(currentMonth, currentMDay)
    if currentMDay == mLastDays[currentMonth] then
        currentMonth = currentMonth + 1
        currentMDay = 1
    else
        currentMDay = currentMDay + 1
    end
    wDayIndex = wDayIndex + 1
end

wDayIndex = wDayIndex % #wDays
print(wDays[wDayIndex + 1])
