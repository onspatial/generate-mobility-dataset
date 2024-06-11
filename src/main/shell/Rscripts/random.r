count <- 90
id_min <- 0
id_max <- 10000
step_min <- 288 * 46
step_max <- 288 * 60


agent_ids <- sample(id_min:id_max, count, replace = FALSE)
cat("agent_ids: ", agent_ids, "\n")
steps <- sample(step_min:step_max, count, replace = FALSE)
cat("steps: ", steps, "\n")
