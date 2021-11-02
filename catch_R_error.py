from subprocess import run

output = run(["Rscript.exe", "tests/test.R"])
if output.returncode != 0:
    raise ValueError("At least one R test has failed")


