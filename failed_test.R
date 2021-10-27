library("multiversion", character.only = T, 
            lib.loc = paste(Sys.getenv('R_VC_LIBRARY_LOCATION'), 
                            'multiversion/0.2.0', sep = '/'))

lib.load(testthat = '3.0.4')

test_that("fail test", {
  expect_equal(1, 0)
})

devtools::test(reporter = c("summary", "fail"))
