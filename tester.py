import subprocess

program = "./John/14.py"
for i in range(1,17):
    program = f"./John/{i}.py"
    with open("./out.log","w") as f:
        process = subprocess.Popen(["bash","./tester.sh",program],shell=False,stdout=f)
        process.wait()
    with open("./out.log","r") as f:
        result = [i.rstrip() for i in f.readlines()]
        if len(result) == 1:
            print(f"{program} failed, took longer than 5m")
        elif int(result[0].split("m")[0]) < 1:
            print(f"{program} passed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}")
        else:
            print(f"{program} failed with time: {result[0].split("m")[0]}m, {result[0].split("m")[1]}, took longer than 1m")
