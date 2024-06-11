# files should be created
# header="header"
# sample_lines="afew test lines"

header="step	simulationTime	location	agentId	neighborhoodId	age	currentMode	currentUnit	family:classroom	lifeStatus	foodNeed:fullness	foodNeed:status	foodNeed:numberOfMealsTaken	sleepNeed:status	shelterNeed:currentShelter	financialSafetyNeed:availableBalance	financialSafetyNeed:job:id	financialSafetyNeed:status	financialSafetyNeed:dailyFoodBudget	financialSafetyNeed:weeklyExtraBudget	loveNeed:meetingId	loveNeed:status	loveNeed:socialStatus	loveNeed:socialHappiness	visitReason	todaysPlan:day	todaysPlan:wakeUpTime	todaysPlan:leaveTimeForWork	todaysPlan:leaveTimeFromWork	todaysPlan:workDay	todaysPlan:beenAtWork	todaysPlan:cameBackFromWork	"
sample_lines="0	2019-07-01T00:00:00.000	POINT (743588.0540441733 3738088.020985135)	0	0	21.083333333333332	AtHome	1	0	Alive	100.0	JustAte	0	Awake	1	-65.39576176054963	1142	Unstable	12.0	0.0	null	NA	0.5	-0.001	None	2019-07-01	07:39:00.000	07:49:00.000	15:59:00.000	true	false	false	"

files=($(find ./ -type f))
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "$header" >"$file"
        echo "$file" >>"$file"
        echo "$sample_lines" >>"$file"
        echo "$sample_lines" >>"$file"
        echo "$sample_lines" >>"$file"
        echo "$file" >>"$file"
    fi
done
