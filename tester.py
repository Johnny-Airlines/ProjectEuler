import subprocess
import sys
from py_markdown_table.markdown_table import markdown_table

def checkFile(program):
    global results
    with open("./out.log","w") as f:
            process = subprocess.Popen(["bash","./tester.sh",program],shell=False,stdout=f)
            process.wait()
    with open("./out.log","r") as f:
        result = [i.rstrip() for i in f.readlines()]
        if len(result) == 1:
            print(f"{program} failed, took longer than 5m")
            results.append({"Problem":i,"result":f"{program} failed, took longer than 5m"})
        elif int(result[0].split("m")[0]) < 1:
            print(f"{program} passed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}")
            results.append({"Problem":i,"result":f"{program} passed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}"})
        else:
            print(f"{program} failed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}, took longer than 1m")
            results.append({"Problem":i,"result":f"{program} failed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}, took longer than 1m"})

options = sys.argv
if len(options) == 1:
    results = []
    for i in range(1,17):
        checkFile(f"./John/{i}.py")
    markdown = markdown_table(results).get_markdown()
    with open("README.md","w") as f:
        f.write("""# ProjectEuler
My attempt at the ProjectEuler problems
"""+markdown.strip("`"))
else:
     checkFile(options[1])
        
