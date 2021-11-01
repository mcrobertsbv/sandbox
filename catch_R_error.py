from subprocess import run

run(["Rscript.exe", "tests/test.R"])
# test_results = output.stdout.decode("utf-8").replace("-", "").replace("=", "").split("\r\n")[1].strip()

