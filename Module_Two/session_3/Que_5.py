# Que_5:- Build a function that takes two lists, one of YouTube video titles and one of their view counts, and returns a list of tuples with each title and its rounded view count (to the nearest thousand using round()).<br><br><em><strong>Hint:</strong> Use zip() to pair titles and counts, and round() inside a list comprehension.</em>

def video_views(titles, views):
    result = [(title, round(view_count, -3))
              for title, view_count in zip(titles, views)]
    return result


titles = ["Python Tutorial", "Gaming Highlights", "Cooking Tips"]
views = [12540, 98765, 43210]

output = video_views(titles, views)

print(output)