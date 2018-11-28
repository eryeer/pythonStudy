tup = (1, 2, 3)
map = {"a": "tom", "b": "jerry"}

print(max(map))

for tup_ele in tup:
    if tup_ele == 2:
        continue
    else:
        print(tup_ele)
else:
    print("loop end")
