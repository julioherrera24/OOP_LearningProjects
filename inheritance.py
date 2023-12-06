""" Below are a few lines describing a problem domain. From this description, identify classes, their state and behavior, and which classes are the child/parent classes of others. You’re designing an online web forum.
On this forum, users will be able to register and log-in, create new threads, and post in existing threads. A thread has a title, its time of creation, and a corresponding collection of posts to that thread. Each post
contains text, the user who posted them, and its time of posting. The system needs to display a thread, which is done by showing each thread’s posts, plus that thread’s metadata. It’s also possible for users to attach
files to posts. Assume there can be many types of files, but you’re primarily interested in image files. A post can have one file attached to it, which will change how it is displayed. Finally, special users called
moderators can edit a post to contain new content."""


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        pass


class Image(File):
    def __init__(self, name, size, image_size):
        super().__init__(name, size)
        self.image_size = image_size


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        pass

    def post(self, thread, content):
        pass

    def make_thread(self, title, content):
        pass


class Moderator(User):
    def edit(self, post, content):
        pass


class Post:
    def __init__(self, user, time_posted, content):
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        print(self.content)


class FilePost(Post):
    def __init__(self, user, time_posted, content, file):
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        print(f"Content: {self.content}\nFile: {self.file.name}")


class Thread:
    def __init__(self, title, time_posted):
        self.title = title
        self.time_posted = time_posted
        self.posts = []

    def display(self):
        pass

    def add_post(self, post):
        self.posts.append(post)
