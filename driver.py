def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())


run("main3.py")
