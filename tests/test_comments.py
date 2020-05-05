# 	import unittest
# from app.models import User, Pitch, Comments
# from app import db
# from datetime import datetime

# class TestModelComment(unittest.TestCase):
# def setUp(self):
#     self.user_her = User(username = 'her', password='Herme', email='her@gmail.com')
#     self.new_pitch = Pitch(title = 'test', content = 'hire me',user_id = 1, category = 'interview')
#     self.new_comment = Comments(id = 1, comment = 'test', user_id = 1, pitch = self.new_pitch)
#     def tearDown(self):
#     Pitch.query.delete()
#     User.query.delete()
# def test_instance_variables(self):
#     self.assertEquals(self.new_comment.id, 1)
#     self.assertEquals(self.new_comment.comment, 'test')
#     self.assertEquals(self.new_comment.user_id, 1)
# def test_save_comment(self):
#     self.new_comment.save_comment()
#     self.assertTrue(len(Comments.query.all()),1)
# def test_save_multiple_comment(self):
#     self.new_comment.save_comment()
#     self.second_her = User(username = 'me', password='Herme', email='me@gmail.com')
#     self.second_pitch = Pitch(title = 'test', content = 'hire',user_id = 2, category = 'interview')
#     self.second_comment = Comments(id = 2, comment = 'test', user_id = 2, pitch = self.new_pitch)
#     self.secpnd_comment.save_comment()
#     self.assertTrue(len(Comments.query.all()),2)


from app.models import Comment,User
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(pitch_id=12345,pitch_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James ) 

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,12345)
        self.assertEquals(self.new_comment.pitch_title,'Review for movies')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.pitch_comment,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user,self.user_James) 

    def test_save_comment(self): 
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)