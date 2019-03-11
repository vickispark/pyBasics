print("DIctionaries,keys must be unique")
monthConv = {
    "jan": "January",
    "Feb": "February",
    "Mar": "March",
    4: "APRIL"
}

print(monthConv.keys())
print(monthConv.values())
print(monthConv["jan"])
print(monthConv.get("Mar"))
print(monthConv.get("dfs", "invalid KEYY"))
print(monthConv[4])
