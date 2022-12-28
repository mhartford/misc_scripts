import os

def print_genre(genre, list):
    print(genre + ":")
    for item in list:
        print(item)

def count_genre(genre, list):
    sort_list = []
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    for item in unique_list:
        count = list.count(item)
        sort_list.append(str(count) + ":" + item)
    sort_list.sort(reverse=True)
    print(genre + ":")
    for item in sort_list:
        print(item)
    unique_list.sort()
    #for item in unique_list:
    #    print(item)

def normalize(a_set):
    if a_set == "Dairy Maid/Eel in the Sink":
        a_set = "The Dairy Maid/The Eel in the Sink"
    if "Bo Mhin Na Toitean" in a_set:
        a_set = "Bo Mhin Na Toitean/Bugle Hornpipe/Drunken Piper"
    if "Mhaigh Eo" in a_set:
        a_set = "Fling Mhaigh Eo/At Matt Molloy's"
    if "REVIEW:" in a_set:
        a_set = a_set.split(":")[1].strip()
    if a_set.startswith("Sonny Murray"):
        a_set = "Sonny Murray's/Home Ruler/Kitty's Wedding"
    if a_set.startswith("Lanigan's"):
        a_set = "Lanigan's Ball/Swallowtail/Kilmovee"
    if a_set.startswith("Night at the Fair"):
        a_set = "Night at the Fair/Eddy Kelly's"
    if a_set.startswith("Morrison's"):
        a_set = "Morrison's/Leitrim/By Golly"
    if a_set.startswith("Silver Spear"):
        a_set = "Silver Spear/Father Kelly's/Miss Monaghan's"
    if a_set.startswith("Tarbolton"):
        a_set = "Tarbolton/Longford Collector/Sailor's Bonnet"
    if a_set.startswith("Jack Coughlan"):
        a_set = "Jack Coughlan's Fancy/McDonagh's/Jenny's Wedding"
    if a_set.startswith("Enchanted Lady"):
        a_set = "Enchanted Lady/Holy Land/Bill Harte's"
    if a_set.startswith("Christmas Eve"):
        a_set = "Christmas Eve/Swingin' on a Gate"
    return a_set

reels = []
jigs = []
hornpipes = []
polkas = []
slides = []
misc = []
inputFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sets.txt")
lines = open(inputFile, 'r').readlines()
for line in lines:
    line = line.strip()
    a_set = line.split(")")[1].split("(")[0].strip()
    a_set = normalize(a_set)
    if "reels" in line:
        reels.append(a_set)
    elif "jigs" in line:
        jigs.append(a_set)
    elif "hornpipes" in line:
        hornpipes.append(a_set)
    elif "polkas" in line:
        polkas.append(a_set)
    elif "slides" in line:
        slides.append(a_set)
    else:
        misc.append(a_set)
    
count_genre("reels", reels)
count_genre("jigs", jigs)
count_genre("hornpipes", hornpipes)
count_genre("polkas", polkas)
count_genre("slides", slides)
count_genre("misc",misc)

