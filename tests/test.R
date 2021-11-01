library("multiversion", character.only = T,
        lib.loc = paste(Sys.getenv('R_VC_LIBRARY_LOCATION'),
                        'multiversion/0.2.0', sep = '/'))

suppressWarnings(lib.load(testthat = '1.0.2', quietly = T))
# library(testthat)
options(testthat.output_file = "test-out.xml")
test_dir("tests/testthat/", reporter = c("Summary", "Fail"))


