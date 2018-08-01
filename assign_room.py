import random
import pprint

rooms = [("Boat Basin: one bedroom, one bath, sleeps four", 4),
         ("Tillamook Nook: studio, one bath, sleeps two", 2),
         ("Clam Cannery: one bedroom, one and a half baths, sleeps four", 4),
         ("Storm Rock: one bedroom, one bath, sleeps six", 6),
         ("Maxwell Point: two bedrooms, two and a half baths, sleeps six", 6 + 1),
         ("Mid Rock Overlook: two bedrooms, two bath, sleeps eight", 4),
         ("Mid Rock Overlook: two bedrooms, two bath, sleeps eight", 4),
         ("Three Arches: one bedroom, one bath, sleeps four", 4),
         ("Chinook: two bedrooms, two baths, sleeps six", 4),
         ("Chinook: two bedrooms, two baths, sleeps six", 2 + 1),
         ("Zeolite: studio, one bath, sleeps two", 2 + 2),
         ("Rosenburg: two bedrooms, one bath, sleeps six", 6 - 2),
         ("Finley Rock: two bedrooms, one bath, sleeps six", 3),
         ("Finley Rock: two bedrooms, one bath, sleeps six", 3),
         ]


parties = [
    ("zxy&wy", 2),
    ("lgang", 4),
    ("zy", 3),
    ("zyj&jpgzh", 7),
    ("wyu", 3),
    ("lym", 3),
    ("xw", 4),
    ("cj", 4),
    ("zsw", 4),
    ("whd", 4),
    ("lh", 4),
    ("lb", 4),
    ("lge", 4),
    ("whxly", 6),
    ]

print "total_capacity: ", sum([count for _, count in rooms])
print "number of persons: ", sum([count for _, count in parties])

random.seed(33)

for size in [1, 2, 3, 4, 6, 7]:
    arooms = filter(lambda x: x[1] == size, rooms)
    aparties = filter(lambda x: x[1] == size, parties)
    random.shuffle(aparties)
    for room, party in zip(arooms, aparties):
        print "%-6s%2d %s" % (party[0], party[1], room[0])
    
    
