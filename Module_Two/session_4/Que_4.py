# Que_4:- Create a mixed tuple called insta_post containing: post_id (int), username (string), likes (int), hashtags (list of strings), and is_public (boolean). Print the tuple and the type of each element.

insta_post = (
    101,
    "vedant_123",
    250,
    ["#python", "#coding", "#learning"],
    True
)

print("Tuple:", insta_post)

print("Type of post_id:", type(insta_post[0]))
print("Type of username:", type(insta_post[1]))
print("Type of likes:", type(insta_post[2]))
print("Type of hashtags:", type(insta_post[3]))
print("Type of is_public:", type(insta_post[4]))