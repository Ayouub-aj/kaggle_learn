# You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# Spaces and punctuation are counted as engraved units.
# Write a function cost_of_project() that takes two arguments:

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold
# It should return the cost of the project. This question should be fairly challenging, and you may need a hint.

def cost_of_project(engraving, solid_gold):
    cost = (solid_gold * (len(engraving) * 10 + 100)) + ((not solid_gold) * (len(engraving) * 7 + 50))
    return cost

print(cost_of_project("Hello, World!", False))  # Should return 141
print(cost_of_project("Hi", True))  # Should return 120
print(cost_of_project("Custom Engraving", True))  # Should return 260
print(cost_of_project("Custom Engraving", False))  # Should return 162