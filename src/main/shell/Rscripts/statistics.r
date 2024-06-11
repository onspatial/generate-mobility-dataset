check_and_install <- function(package) {
  if (!require(package, character.only = TRUE)) {
    install.packages(package, dependencies = TRUE, repos = "https://cloud.r-project.org/")
    library(package, character.only = TRUE)
  }
}


check_and_install("readr")


library(readr)


input <- "full.data.tsv"

args <- commandArgs(trailingOnly = TRUE)
if (length(args) > 0) {
  input <- args[1]
  cat("default input file changed to ", input, "\n")
}


data <- read_tsv(input)

head(data)

mean_age <- mean(data$age, na.rm = TRUE)
median_age <- median(data$age, na.rm = TRUE)
age_range <- range(data$age, na.rm = TRUE)
age_sd <- sd(data$age, na.rm = TRUE)
age_iqr <- IQR(data$age, na.rm = TRUE)
age_min <- min(data$age, na.rm = TRUE)
age_max <- max(data$age, na.rm = TRUE)
age_q1 <- quantile(data$age, 0.25, na.rm = TRUE)
age_q3 <- quantile(data$age, 0.75, na.rm = TRUE)



# cat('simulationTime:',"\n")
# (param_freq <- table(data$'simulationTime'))
# cat('location:',"\n")
# (param_freq <- table(data$'location'))
# cat('agentId:',"\n")
# (param_freq <- table(data$'agentId'))
# cat('neighborhoodId:',"\n")
# (param_freq <- table(data$'neighborhoodId'))
# cat('age:',"\n")
# (param_freq <- table(data$'age'))
cat('currentMode:',"\n")
(param_freq <- table(data$'currentMode'))
# cat('currentUnit:',"\n")
# (param_freq <- table(data$'currentUnit'))
cat('family:classroom:',"\n")
(param_freq <- table(data$'family:classroom'))
cat('lifeStatus:',"\n")
(param_freq <- table(data$'lifeStatus'))
# cat('foodNeed:fullness:',"\n")
# (param_freq <- table(data$'foodNeed:fullness'))
cat('foodNeed:status:',"\n")
(param_freq <- table(data$'foodNeed:status'))
cat('foodNeed:numberOfMealsTaken:',"\n")
(param_freq <- table(data$'foodNeed:numberOfMealsTaken'))
# cat('sleepNeed:status:',"\n")
# (param_freq <- table(data$'sleepNeed:status'))
# cat('shelterNeed:currentShelter:',"\n")
# (param_freq <- table(data$'shelterNeed:currentShelter'))
# cat('financialSafetyNeed:availableBalance:',"\n")
# (param_freq <- table(data$'financialSafetyNeed:availableBalance'))
# cat('financialSafetyNeed:job:id:',"\n")
# (param_freq <- table(data$'financialSafetyNeed:job:id'))
# cat('financialSafetyNeed:status:',"\n")
# (param_freq <- table(data$'financialSafetyNeed:status'))
# cat('financialSafetyNeed:dailyFoodBudget:',"\n")
# (param_freq <- table(data$'financialSafetyNeed:dailyFoodBudget'))
# cat('financialSafetyNeed:weeklyExtraBudget:',"\n")
# (param_freq <- table(data$'financialSafetyNeed:weeklyExtraBudget'))
cat('loveNeed:meetingId:',"\n")
(param_freq <- table(data$'loveNeed:meetingId'))
cat('loveNeed:status:',"\n")
(param_freq <- table(data$'loveNeed:status'))
# cat('loveNeed:socialStatus:',"\n")
# (param_freq <- table(data$'loveNeed:socialStatus'))

cat('visitReason:',"\n")
(param_freq <- table(data$'visitReason'))
# cat('todaysPlan:day:',"\n")
# (param_freq <- table(data$'todaysPlan:day'))
# cat('todaysPlan:wakeUpTime:',"\n")
# (param_freq <- table(data$'todaysPlan:wakeUpTime'))
# cat('todaysPlan:leaveTimeForWork:',"\n")
# (param_freq <- table(data$'todaysPlan:leaveTimeForWork'))
# cat('todaysPlan:leaveTimeFromWork:',"\n")
# (param_freq <- table(data$'todaysPlan:leaveTimeFromWork'))
cat('todaysPlan:workDay:',"\n")
(param_freq <- table(data$'todaysPlan:workDay'))
cat('todaysPlan:beenAtWork:',"\n")
(param_freq <- table(data$'todaysPlan:beenAtWork'))
cat('todaysPlan:cameBackFromWork:',"\n")
(param_freq <- table(data$'todaysPlan:cameBackFromWork'))

# cat('loveNeed:socialHappiness:',"\n")
# (param_freq <- table(data$'loveNeed:socialHappiness'))


cat("mean age: ", mean_age, "\n")
cat("median age: ", median_age, "\n")
cat("age range: ", age_range, "\n")
cat("age sd: ", age_sd, "\n")
cat("age iqr: ", age_iqr, "\n")
cat("age min: ", age_min, "\n")
cat("age max: ", age_max, "\n")
cat("age q1: ", age_q1, "\n")
cat("age q3: ", age_q3, "\n")

#sed -n '82730754, 123796673p'  full.data.tsv > full.data.normal.tsv