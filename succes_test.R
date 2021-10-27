library("multiversion", character.only = T, 
            lib.loc = paste(Sys.getenv('R_VC_LIBRARY_LOCATION'), 
                            'multiversion/0.2.0', sep = '/'))

lib.load(testthat = '1.0.2')

test_that("expect success", {
          expect_equal(1, 1)
})
