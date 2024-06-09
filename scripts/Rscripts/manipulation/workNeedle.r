library(jsonlite)
set.seed(63)
count <- 30
id_min <- 0
id_max <- 1000
start_step <- 129600
days <- 288


agent_ids <- sample(id_min:id_max, count, replace = FALSE)
agent_ids_1 <- agent_ids[1:10]
agent_ids_2 <- agent_ids[11:20]
agent_ids_3 <- agent_ids[21:30]



json_set_needle <- '{
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

json_type_needle <- '{
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
data_set_needle <- fromJSON(json_set_needle)
data_type_needle <- fromJSON(json_type_needle)



cat("[", "\n")
# green needle
for (id in agent_ids_1) {
    data_set_needle$id <- id
    data_set_needle$value <- 0.2
    data_set_needle$steps <- start_step
    cat(toJSON(data_set_needle, auto_unbox = TRUE), ",", "\n")

}
# yellow needle
for (id in agent_ids_2) {
    data_set_needle$id <- id
    data_set_needle$value <- 0.5
    data_set_needle$steps <- start_step
    cat(toJSON(data_set_needle, auto_unbox = TRUE), ",", "\n")
   
}
# red needle
for (id in agent_ids_3) {
    data_set_needle$id <- id
    data_set_needle$value <- 1
    data_set_needle$steps <- start_step
    cat(toJSON(data_set_needle, auto_unbox = TRUE), ",", "\n")
    
}

# green needle
for (id in agent_ids_1) {
    data_type_needle$id <- id
    data_type_needle$steps <- start_step
    cat(toJSON(data_type_needle, auto_unbox = TRUE), ",", "\n")
}
# yellow needle
for (id in agent_ids_2) {
    data_type_needle$id <- id
    data_type_needle$steps <- start_step
    cat(toJSON(data_type_needle, auto_unbox = TRUE), ",", "\n")
}
# red needle
for (id in agent_ids_3) {
    data_type_needle$id <- id
    data_type_needle$steps <- start_step
    cat(toJSON(data_type_needle, auto_unbox = TRUE), ",", "\n")
}
cat("]", "\n")