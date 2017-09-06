x = [4, 6, 1, 3, 5, 7, 25]
xy = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(num_list):
    for num in num_list:
        star_line = ""
        star_line += "*"*num
        print star_line

draw_stars(x)

print "now the Part II"

def draw_stars2(num_list):
    for thing in num_list:
        if isinstance(thing, int):
            star_line = ""
            star_line += "*"*thing
            print star_line

        elif isinstance(thing, str):
            str_line = ""
            str_line += thing[0].lower() * len(thing)
            print str_line
            
draw_stars2(xy)