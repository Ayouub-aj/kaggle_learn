# You can actually use Python to quickly turn this string into a list with .split(). 
# In the parentheses, we need to provide the character should be used to mark the end of one list item and the beginning of another, and enclose it in quotation marks. 
# In this case, that character is a comma.

# uncomment example to see how it works:
# flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
#  print(flowers.split(","))

# Now it is your turn to try this out!  Create two Python lists:
# - `letters` should be a Python list where each entry is an uppercase letter of the English alphabet.  For instance, the first two entries should be `"A"` and `"B"`, 
# and the final two entries should be `"Y"` and `"Z"`.  Use the string `alphabet` to create this list.
# - `address` should be a Python list where each row in `address` is a different item in the list.  Currently, each row in `address` is separated by a comma. 

# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split(".")
formatted_address = address.split(",")

#run on your own terminal to see results
# print(letters)
# print(formatted_address)