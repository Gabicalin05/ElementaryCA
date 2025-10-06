count = 0

def draw(vector):
    l = ""
    for i in vector:
        l += i
    print(l)

def rules(left, current, right):
    # neighbors to binary digits
    bits = []

    for bit in [left, current, right]:
        if bit == "1":
            bits.append("1")
        else:
            bits.append("0")

    neighborhood = ''.join(bits)

    # back to int and flipped
    index = 7 - int(neighborhood, 2)
    return ruleset[index]

# generation 0
n_cells = 101
generation = [" "] * n_cells
generation[n_cells // 2] = "1"

rule_select = int(input("Choose a rule from 0 to 255: "))

# convert to binary
conversion = format(rule_select, "08b")

ruleset = []
for bit in conversion:
    if bit == "1":
        ruleset.append("1")
    else:
        ruleset.append(" ")

draw(generation)
while count < 100:
    n = len(generation)
    newGen = []
    for i in range(n):
        left = generation[(i - 1) % n]
        current = generation[i]
        right = generation[(i + 1) % n]
        newGen.append(rules(left, current, right))

    generation = newGen
    draw(generation)
    count += 1