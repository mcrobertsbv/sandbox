library("multiversion", character.only = T,
        lib.loc = paste(Sys.getenv('R_VC_LIBRARY_LOCATION'),
                        'multiversion/0.2.0', sep = '/'))

suppressWarnings(lib.load(testthat = '3.1.0', quietly = T))

options(testthat.output_file = "./tests/R_test_out.xml")
test_dir("tests/testthat/", reporter = "Junit")


