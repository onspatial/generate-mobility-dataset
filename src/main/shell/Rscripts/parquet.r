check_and_install <- function(package) {
  if (!require(package, character.only = TRUE)) {
    install.packages(package, dependencies = TRUE, repos = "https://cloud.r-project.org/")
    library(package, character.only = TRUE)
  }
}


check_and_install("arrow")
check_and_install("data.table")


library(arrow)


input <- "data.parquet"

args <- commandArgs(trailingOnly = TRUE)
if (length(args) > 0) {
  input <- args[1]
  cat("default input file changed to ", input, "\n")
}
data <- read_parquet(input)
data <- as.data.table(data)
head(data)

(data[,.(VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, PULocationID, DOLocationID) ])

