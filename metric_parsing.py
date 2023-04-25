import re

txt = "¾ cup brown sugar"

recipeTXT = ['4 tablespoons tsp olive oil','2 cups chopped leeks, white part only (from approximately 3 medium leeks)','2 tablespoons finely minced garlic','Kosher salt','2 cups carrots, peeled and chopped into rounds (approximately 2 medium)','2 cups peeled and diced potatoes','2 cups fresh green beans, broken or cut into 3/4-inch pieces','2 quarts chicken or vegetable broth','4 cups peeled, seeded, and chopped tomatoes','2 ears corn, kernels removed','1/2 teaspoon freshly ground black pepper','1/4 cup packed, chopped fresh parsley leaves','1 to 2 teaspoons freshly squeezed lemon juice']


#Check if the string contains either "falls" or "stays":

def metric_search(ingredient):
    metric = []
    x = re.findall("cup", ingredient)
    if (x):
        metric.append('cup')
    x = re.findall("quart|quarts|qt", ingredient)
    if (x):
        metric.append('quart')
    x = re.findall("gallon|gal", ingredient)
    if (x):
        metric.append('gallon')
    x = re.findall("pint|pt", ingredient)
    if (x):
        metric.append('pint')
    x = re.findall("tablespoon|tbsp|tbs", ingredient)
    if (x):
        metric.append('tablespoon')
    x = re.findall("teaspoon|tsp", ingredient)
    if (x):
        metric.append('teaspoon')
    x = re.findall("eggs|egg", ingredient)
    if (x):
        metric.append('egg')
    x = re.findall("ounce|oz", ingredient)
    if (x):
    	metric.append('ounce')
    
    if len(metric) > 1:
    	print(" NOTE : Multiple metrics detected")
   
    amount = re.split("\s", ingredient)[0]
		#splits ingredient string into array of strings by whitespace character, takes the first
		## e.g.: ingredient = 2 cups all-purpose flour
        ### re.split("\s", ingredient)     =  ['2','cups','all-purpose','flour']
        ### re.split("\s", ingredient)[0]  =  ['2']
        
    metric = [amount] + metric
    
    
    return(metric)

for item in recipeTXT:
	print(item)
	print('	', metric_search(item))


cup_search = re.findall("cups|c.", txt)
quart_search = re.findall("quart|quarts|qt", txt)
gallon_search = re.findall("gallon|gal", txt)
pint_search = re.findall("pint|pt", txt)
tbsp_search = re.findall("tablespoon|tbsp|tbs", txt)
tsp_search = re.findall("teaspoon|tsp", txt)
egg_search = re.findall("eggs|egg", txt)

x = cup_search

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
