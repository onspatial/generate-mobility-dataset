library(jsonlite)
set.seed(63)
count <- 90
id_min <- 0
id_max <- 1000
values_keep_full <- c(0, 0.5, 0.75)
values_fullness_decrease <- c(3, 2, 1.5)

agent_ids <- sample(id_min:id_max, count, replace = FALSE)

agent_ids_1 <- agent_ids[1:30]
agent_ids_2 <- agent_ids[31:60]
agent_ids_3 <- agent_ids[61:90]

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

data_keep_full <- fromJSON(json_keep_full)
data_fullness_decrease <- fromJSON(json__fullness_decrease)

print(values_keep_full)
cat("[", "\n")
for (i in seq(1, length(agent_ids_1), 3)) {
    data_keep_full$id <- agent_ids_1[i]
    data_keep_full$value <- values_keep_full[1]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_1[i + 1]
    data_keep_full$value <- values_keep_full[2]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_1[i + 2]
    data_keep_full$value <- values_keep_full[3]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")
}
# cat("]\n")



# print(values_fullness_decrease)

# cat("[", "\n")
for (i in seq(1, length(agent_ids_1), 3)) {
    data_fullness_decrease$id <- agent_ids_1[i]
    data_fullness_decrease$value <- values_fullness_decrease[1]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_1[i + 1]
    data_fullness_decrease$value <- values_fullness_decrease[2]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_1[i + 2]
    data_fullness_decrease$value <- values_fullness_decrease[3]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")
}

for (i in seq(1, length(agent_ids_2), 3)) {
    data_keep_full$id <- agent_ids_2[i]
    data_keep_full$value <- values_keep_full[1]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_2[i + 1]
    data_keep_full$value <- values_keep_full[2]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")

    data_keep_full$id <- agent_ids_2[i + 2]
    data_keep_full$value <- values_keep_full[3]
    cat(toJSON(data_keep_full, auto_unbox = TRUE), ",", "\n")
}
# cat("]\n")



# print(values_fullness_decrease)

# cat("[", "\n")
for (i in seq(1, length(agent_ids_3), 3)) {
    data_fullness_decrease$id <- agent_ids_3[i]
    data_fullness_decrease$value <- values_fullness_decrease[1]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_3[i + 1]
    data_fullness_decrease$value <- values_fullness_decrease[2]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")

    data_fullness_decrease$id <- agent_ids_3[i + 2]
    data_fullness_decrease$value <- values_fullness_decrease[3]
    cat(toJSON(data_fullness_decrease, auto_unbox = TRUE), ",", "\n")
}
cat("]\n")

red_index = seq(1, length(agent_ids), 3)
yellow_index = seq(2, length(agent_ids), 3)
green_index = seq(3, length(agent_ids), 3)

cat("ALL:", agent_ids, "\n")
cat("RED:", agent_ids[red_index], "\n")
cat("YELLOW:", agent_ids[yellow_index], "\n")
cat("GREEN:", agent_ids[green_index], "\n")
