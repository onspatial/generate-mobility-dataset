library(jsonlite)
set.seed(63)
count <- 30 + 30 + 90
id_min <- 0
id_max <- 3000
start_step <- 129600
days <- 288
values_keep_full <- c(0, 0.5, 0.75)
values_fullness_decrease <- c(3, 2, 1.5)

agent_ids <- sample(id_min:id_max, count, replace = FALSE)
# each set includes red yellow and green
agent_ids_hungry_set1 <- agent_ids[1:30] 
agent_ids_hungry_set2 <- agent_ids[31:60]
agent_ids_hungry_set3 <- agent_ids[61:90]

agent_ids_social_red <- agent_ids[91:100]
agent_ids_social_yellow <- agent_ids[101:110]
agent_ids_social_green <- agent_ids[111:120]

agent_ids_work_red <- agent_ids[121:130]
agent_ids_work_yellow <- agent_ids[131:140]
agent_ids_work_green <- agent_ids[141:150]

json_keep_full <- '{
        "actor": "PERSON",
        "id": 0,
        "steps": 129600,
        "operator": "MULTIPLY",
        "fieldName": "keepingFullTimeInMinutes",
        "value": "0",
        "accessors": [
          {
            "manipulationType": "FIELD",
            "name": "foodNeed"
          }
        ]
    }'

json__fullness_decrease <- '{
        "actor": "PERSON",
        "id": 0,
        "steps": 129600,
        "operator": "MULTIPLY",
        "fieldName": "fullnessDecreasePerStep",
        "value": "0",
        "accessors": [
          {
            "manipulationType": "FIELD",
            "name": "foodNeed"
          }
        ]
    }'

json_set_needle_social <- '{
        "actor": "PERSON",
        "id": 101,
        "steps": 100,
        "operator": "SET",
        "fieldName": "chanceToBeNeedle",
        "value": 0.1,
        "accessors": [
            {
                "manipulationType": "FIELD",
                "name": "needle"
            }
        ]
    }'

json_type_needle_social <- '{
        "actor": "PERSON",
        "id": 101,
        "steps": 100,
        "accessors": [
            {
                "manipulationType": "METHOD",
                "name": "setNeedleType",
                "parameters": ["Social"]
            }
        ]
    }'

json_set_needle_work <- '{
        "actor": "PERSON",
        "id": 101,
        "steps": 100,
        "operator": "SET",
        "fieldName": "chanceToBeNeedle",
        "value": 0.1,
        "accessors": [
            {
                "manipulationType": "FIELD",
                "name": "needle"
            }
        ]
    }'

json_type_needle_work <- '{
        "actor": "PERSON",
        "id": 101,
        "steps": 100,
        "accessors": [
            {
                "manipulationType": "METHOD",
                "name": "setNeedleType",
                "parameters": ["Work"]
            }
        ]
    }'


data_keep_full <- fromJSON(json_keep_full)
data_fullness_decrease <- fromJSON(json__fullness_decrease)

data_set_needle_social <- fromJSON(json_set_needle_social)
data_type_needle_social <- fromJSON(json_type_needle_social)

data_type_needle_work <- fromJSON(json_type_needle_work)
data_set_needle_work <- fromJSON(json_set_needle_work)



print(values_keep_full)
cat("[", "\n")
for (i in seq(1, length(agent_ids_hungry_set1), 3)) {
    data_keep_full$id <- agent_ids_hungry_set1[i]
    data_keep_full$value <- values_keep_full[1]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_hungry_set1[i + 1]
    data_keep_full$value <- values_keep_full[2]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_hungry_set1[i + 2]
    data_keep_full$value <- values_keep_full[3]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")
}

for (i in seq(1, length(agent_ids_hungry_set1), 3)) {
    data_fullness_decrease$id <- agent_ids_hungry_set1[i]
    data_fullness_decrease$value <- values_fullness_decrease[1]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_hungry_set1[i + 1]
    data_fullness_decrease$value <- values_fullness_decrease[2]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_hungry_set1[i + 2]
    data_fullness_decrease$value <- values_fullness_decrease[3]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")
}

for (i in seq(1, length(agent_ids_hungry_set2), 3)) {
    data_keep_full$id <- agent_ids_hungry_set2[i]
    data_keep_full$value <- values_keep_full[1]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_hungry_set2[i + 1]
    data_keep_full$value <- values_keep_full[2]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_hungry_set2[i + 2]
    data_keep_full$value <- values_keep_full[3]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")
}

for (i in seq(1, length(agent_ids_hungry_set3), 3)) {
    data_fullness_decrease$id <- agent_ids_hungry_set3[i]
    data_fullness_decrease$value <- values_fullness_decrease[1]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_hungry_set3[i + 1]
    data_fullness_decrease$value <- values_fullness_decrease[2]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_hungry_set3[i + 2]
    data_fullness_decrease$value <- values_fullness_decrease[3]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")
}




# social needles
# green needle
for (id in agent_ids_social_green) {
    data_set_needle_social$id <- id
    data_set_needle_social$value <- 0.2
    data_set_needle_social$steps <- start_step
    cat(toJSON(data_set_needle_social, auto_unbox = TRUE), ",", "\n")

}
# yellow needle
for (id in agent_ids_social_yellow) {
    data_set_needle_social$id <- id
    data_set_needle_social$value <- 0.5
    data_set_needle_social$steps <- start_step
    cat(toJSON(data_set_needle_social, auto_unbox = TRUE), ",", "\n")
   
}
# red needle
for (id in agent_ids_social_red) {
    data_set_needle_social$id <- id
    data_set_needle_social$value <- 1
    data_set_needle_social$steps <- start_step
    cat(toJSON(data_set_needle_social, auto_unbox = TRUE), ",", "\n")
    
}

# green needle
for (id in agent_ids_social_green) {
    data_type_needle_social$id <- id
    data_type_needle_social$steps <- start_step
    cat(toJSON(data_type_needle_social, auto_unbox = TRUE), ",", "\n")
}
# yellow needle
for (id in agent_ids_social_yellow) {
    data_type_needle_social$id <- id
    data_type_needle_social$steps <- start_step
    cat(toJSON(data_type_needle_social, auto_unbox = TRUE), ",", "\n")
}
# red needle
for (id in agent_ids_social_red) {
    data_type_needle_social$id <- id
    data_type_needle_social$steps <- start_step
    cat(toJSON(data_type_needle_social, auto_unbox = TRUE), ",", "\n")
}




# work needles
# green needle
for (id in agent_ids_work_green) {
    data_set_needle_work$id <- id
    data_set_needle_work$value <- 0.2
    data_set_needle_work$steps <- start_step
    cat(toJSON(data_set_needle_work, auto_unbox = TRUE), ",", "\n")

}
# yellow needle
for (id in agent_ids_work_yellow) {
    data_set_needle_work$id <- id
    data_set_needle_work$value <- 0.5
    data_set_needle_work$steps <- start_step
    cat(toJSON(data_set_needle_work, auto_unbox = TRUE), ",", "\n")
   
}
# red needle
for (id in agent_ids_work_red) {
    data_set_needle_work$id <- id
    data_set_needle_work$value <- 1
    data_set_needle_work$steps <- start_step
    cat(toJSON(data_set_needle_work, auto_unbox = TRUE), ",", "\n")
    
}

# green needle
for (id in agent_ids_work_green) {
    data_type_needle_work$id <- id
    data_type_needle_work$steps <- start_step
    cat(toJSON(data_type_needle_work, auto_unbox = TRUE), ",", "\n")
}
# yellow needle
for (id in agent_ids_work_yellow) {
    data_type_needle_work$id <- id
    data_type_needle_work$steps <- start_step
    cat(toJSON(data_type_needle_work, auto_unbox = TRUE), ",", "\n")
}
# red needle
for (id in agent_ids_work_red) {
    data_type_needle_work$id <- id
    data_type_needle_work$steps <- start_step
    cat(toJSON(data_type_needle_work, auto_unbox = TRUE), ",", "\n")
}
cat("]", "\n")

cat("-----------------------------------", "\n")


print("hungry needles:")
print("SET1:")
cat("RED:", agent_ids_hungry_set1[1:10], "\n")
cat("YELLOW:", agent_ids_hungry_set1[11:20], "\n")
cat("GREEN", agent_ids_hungry_set1[21:30], "\n")

print("SET2:")
cat("RED:", agent_ids_hungry_set2[1:10], "\n")
cat("YELLOW:", agent_ids_hungry_set2[11:20], "\n")
cat("GREEN", agent_ids_hungry_set2[21:30], "\n")

print("SET3:")
cat("RED:", agent_ids_hungry_set3[1:10], "\n")
cat("YELLOW:", agent_ids_hungry_set3[11:20], "\n")
cat("GREEN", agent_ids_hungry_set3[21:30], "\n")

print("work needles :")
cat("RED:", agent_ids_work_red, "\n")
cat("YELLOW:", agent_ids_work_yellow, "\n")
cat("GREEN", agent_ids_work_green, "\n")

print("social needles :")
cat("RED:", agent_ids_social_red, "\n")
cat("YELLOW:", agent_ids_social_yellow, "\n")
cat("GREEN", agent_ids_social_green, "\n")