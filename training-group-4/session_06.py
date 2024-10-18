import json

print("hello")


texts = [
    "Da rufele la rusi",
    "Ana are mere",
    "Ciresel vine si cere",
    "Catelus cu parul cret",
    "Da rufele la rusi",
    "Catelus cu parul cret",
]

some_objects = list()
address = dict(
    first_name="Radu",
    last_name="Apostol",
    street="Bana",
    number="tz",
    zipcode="sh",
    extension="k",
)
replacements = {
    "A": "Bana",
    "t": "tz",
    "s": "sh",
    "c": "k",
    10: 222,
    "placeholder": None,
    True: {
        "left": "right",
        "up": "down",
    },
}


replacements["C"] = "K"
print(replacements)
print("s" in replacements)
print(10 in replacements)
print("test" in replacements)

for line in texts:
    print("original:", line)
    transformed = ""
    for letter in line:
        transformed += replacements.get(letter, letter)
    print("transformed:", transformed)


print("--" * 20)

# saving replacement dict to a json file
with open("banana.json", "wt") as output_file:
    # NOTE: "wt" means "write text"
    output_file.write(json.dumps(replacements))

# parse json datafile
with open("cars.json") as data_file:
    # NOTE: read entire file in memory under the content variable
    content = data_file.read()   
    print(content)
    print(type(content), len(content))

    # NOTE: analize content and extracts meaningful data from json
    data = json.loads(content)
    print(type(data), len(data))

# traverse loaded data to look for interesting cases
for obj in data[:3]:
    # just print all key -> values
    for key, value in obj.items():
        print(key, "=>", value)

    # look for models that are not numeric
    brand = obj["brand"]
    if "models" not in obj:
        print(brand, "has no model")
    else:
        models = obj["models"]
        for model in models:
            title = model["title"]
            if not title.isnumeric():
                print(brand, title)




