import subprocess
import sys
from tabulate import tabulate
import json
import os

def checkFile(program,update = False):
    global results
    global i
    try:
        with open("./out.log","w+") as f:
            process = subprocess.run(["bash","./tester.sh",program],shell=False,stdout=f,timeout=300)
        with open("./out.log","r") as f:
            result = [i.rstrip() for i in f.readlines()]
        if process.returncode == 1:
            print(f"{program} failed, wrong value")
            formattedRes = [i,"❌","-","Wrong value"]
        elif process.returncode != 0:
            print(f"{program} failed with exit code {process.returncode}, probably crashed")
            formattedRes = [i,"❌","-",f"Exit code: {process.returncode}"]
        elif int(result[0].split("m")[0]) < 1:
            print(f"{program} passed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}")
            formattedRes = [i,"✅",f"{result[0].split("m")[0]}m, {result[0].split("m")[1]}","-"]
        else:
            print(f"{program} failed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}, took longer than 1m")
            formattedRes = [i,"❌",f"{result[0].split("m")[0]}m, {result[0].split("m")[1]}", "took longer than 1m"]
        os.remove("./out.log")
    except subprocess.TimeoutExpired:
        print(f"{program} failed, took longer than 5m")
        formattedRes = [i,"❌","-",f"Took longer than 5m"]
    if update:
        if i <= len(results):
            results.pop(i-1)
        results.insert(i-1,formattedRes)
    else:
        results.append(formattedRes)

options = sys.argv
if len(options) == 1:
    results = []
    for i in range(1,18):
        checkFile(f"./John/{i}.py")
    
else:
    with open("./results.json","r") as f:
        results = json.load(f)
    i = int(options[1])
    checkFile(f"./John/{options[1]}.py",True)

with open("./results.json","w") as f:
    json.dump(results,f)
markdown = tabulate(results,["Problem","Result","Time","Reason"],tablefmt="github")
with open("README.md","w") as f:
    f.write("""# ProjectEuler
My attempt at the ProjectEuler problems
"""+markdown)
