# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])

# Add element to set
A.add("NSYNC")

#remove
A.remove("NSYNC")

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Find the intersections
intersection = album_set1 & album_set2

# Find the difference in set1 but not set2




print(set1)
print(album_set)
print(music_genres)
print(A)
print("AC/DC" in A)
print(album_set1, album_set2)
print(intersection)
print(album_set1.difference(album_set2))
print(album_set2.difference(album_set1))
# Use intersection method to find the intersection of album_list1 and album_list2
print(album_set1.intersection(album_set2) )  

# Find the union of two sets
print(album_set1.union(album_set2))

# Check if superset
print(set(album_set1).issuperset(album_set2))
   
# Check if subset
print(set(album_set2).issubset(album_set1) )

# Check if subset
print(set({"Back in Black", "AC/DC"}).issubset(album_set1))
 
# Check if superset
print(album_set1.issuperset({"Back in Black", "AC/DC"}))
   
print(len(("disco",10,1.2, "hard rock",10)))