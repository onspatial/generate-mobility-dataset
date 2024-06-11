library(jsonlite)
set.seed(63)
count <- 30
id_min <- 0
id_max <- 10000
start_step <- 13248
days <- 288


agent_ids <- sample(id_min:id_max, count, replace = FALSE)
agent_ids_1 <- agent_ids[1:10]
agent_ids_2 <- agent_ids[11:20]
agent_ids_3 <- agent_ids[21:30]


json_is_needle <- '{
        "actor": "PERSON",
        "id": 0,
        "steps": 101,
        "operator": "SET",
        "fieldName": "isNeedle",
        "value": true,
        "accessors": []
    }'

data_is_needle <- fromJSON(json_is_needle)

cat("[", "\n")
# green needle
for (id in agent_ids_1) {
    data_is_needle$id <- id
    data_is_needle$value <- TRUE
    data_is_needle$steps <- start_step
    cat(toJSON(data_is_needle, auto_unbox = TRUE), ",", "\n")
    data_is_needle$steps <- start_step + 3 * days
    data_is_needle$value <- FALSE
    cat(toJSON(data_is_needle, auto_unbox = TRUE), ",", "\n")
}
# yellow needle
for (id in agent_ids_2) {
    data_is_needle$id <- id
    data_is_needle$value <- TRUE
    data_is_needle$steps <- start_step
    cat(toJSON(data_is_needle, auto_unbox = TRUE), ",", "\n")
    data_is_needle$steps <- start_step + 7 * days
    data_is_needle$value <- FALSE
    cat(toJSON(data_is_needle, auto_unbox = TRUE), ",", "\n")
}
# red needle
for (id in agent_ids_3) {
    data_is_needle$id <- id
    data_is_needle$value <- TRUE
    data_is_needle$steps <- start_step
    cat(toJSON(data_is_needle, auto_unbox = TRUE), ",", "\n")
}
cat("]", "\n")