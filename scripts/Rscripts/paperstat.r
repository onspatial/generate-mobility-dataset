input <- "full.data.tsv"

args <- commandArgs(trailingOnly = TRUE)
if (length(args) > 0) {
  input <- args[1]
  cat("default input file changed to ", input, "\n")
}


data <- read_tsv(input)
cat('currentMode:',"\n")
(param_freq <- table(data$'currentMode'))
