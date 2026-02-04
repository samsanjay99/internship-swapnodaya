class Instagram:
    def __init__(self, title, description, creator_name, location):  
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = [] 

    def display_title(self):
        print(f"The title of the reel is: {self.title}")

    def display_description(self):
        print(f"The description of the reel is: {self.description}")

    def display_creator_info(self):
        print(f"Posted by: {self.creator_name} in {self.location}")

    def display_likes(self):
        print(f"Likes: {self.likes}")

    def add_comment(self, comment_text):
        self.comments.append(comment_text)

    def display_comments(self):
        print(f"--- Comments on '{self.title}' ---")
        if not self.comments:
            print("No comments yet.")
        for comment in self.comments:
            print(f"- {comment}")

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1
    
    def delete_last_comment(self):
        if len(self.comments) > 0:
            removed = self.comments.pop()
            print(f"Deleted last comment: '{removed}'")
        else:
            print("No comments to delete!")

# --- Execution ---

# Creating instances with the new attributes
reel1 = Instagram("dancing", "dancing with friends", "DanceQueen_99", "Los Angeles")
reel2 = Instagram("finance minister conference", "Live updates", "EconomyDaily", "New Delhi")


reel1.add_comment("Great moves!")
reel1.add_comment("What song is this?")
reel1.add_comment("What song ")


reel1.liked()
reel1.liked()
reel2.liked()

reel1.display_title()
reel1.display_creator_info()
reel1.display_likes()
reel1.display_comments()
reel1.delete_last_comment()
print("-" * 20)

reel2.display_creator_info()
reel2.display_likes()
reel2.display_comments()