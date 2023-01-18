import pathlib

p_str = ("./Inputs/", "./Noisy/", "./Filtered/", "./Original/")

for i in p_str:
    p = pathlib.Path(i)
    p.mkdir(parents=True, exist_ok= True)