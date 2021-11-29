library("multiversion", character.only = T,
        lib.loc = paste(Sys.getenv('R_VC_LIBRARY_LOCATION'),
                        'multiversion/0.2.0', sep = '/'))

suppressWarnings(lib.load(rlang = "0.4.11", 
                          tibble = "3.1.5",
                          rematch2 = "2.1.2", 
                          testthat = '3.1.0', 
                          rprojroot = "2.0.2", 
                          xml2 = "1.1.1",
                          quietly = T)
)

options(testthat.output_file = "./tests/R_test_out.xml")
test_dir("tests/testthat/", reporter = "Junit")


