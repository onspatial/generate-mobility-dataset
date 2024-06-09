check_and_install <- function(package) {
  if (!require(package, character.only = TRUE)) {
    install.packages(package, dependencies = TRUE, repos = "https://cloud.r-project.org/")
    library(package, character.only = TRUE)
  }
}


check_and_install("readr")
check_and_install("DBI")
check_and_install("RSQLite")

library(readr)
library(DBI)
library(RSQLite)

input <- "full.data.tsv"
database <- "full.data.db"
table <- "table"

args <- commandArgs(trailingOnly = TRUE)
if (length(args) > 0) {
  input <- args[1]
  database <- paste0(input, ".db")
  cat("default input file changed to ", input, "\n")
  cat("default database file changed to ", database, "\n")
}


df <- read_tsv(input)
con <- dbConnect(RSQLite::SQLite(), database)
dbWriteTable(con, table, df, append = TRUE, row.names = FALSE)
dbDisconnect(con)
