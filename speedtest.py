import timeit

print(timeit.timeit('subprocess.run(f"{sys.executable} the2tester.py", shell=1, stdout=subprocess.PIPE)', number=1, setup = "import subprocess, sys"))