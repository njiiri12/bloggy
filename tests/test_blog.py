import unittest
from app.models  import User,Blog,Comment
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_njiiri = User(username="njiiri",password="Jamlick12",email="njerinjiiri@gmail.com")
        self.new_blog = Blog(id="1",title="testing",content="testing blog",user_id=self.user_njiiri)
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_blog.title, 'testing')  
        self.assertEquals(self.new_blog.content, 'testing blog')   
        self.assertEquals(self.new_blog.user_id,self.user_njiiri)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()> 0))

    def test_get_blog(self):
        self.new_blog.save_blog()
        g_blog = Blog.get_blog(1)
        self.assertTrue(g_blog is not None)

class CommentTest(unittest.TestCase):
    def setUp(self):
        self.user_njiiri = User(username= 'njiiri',email='njerinjiiri@gmail.com',password = 'Jamlick12')
        self.new_blog = Blog(id=1,title='test',content='a test blog',user_id=self.user_kenya)
        self.new_comment= Comment(id=1,comment='test comment',blog_id=self.new_blog.id,user_id=self.user_kenya)

    def tearDown(self):
        User.query.delete()
        Comment.query.delete()
        Blog.query.delete()
        
    def test_check_instance(self):
        self.assertEquals(self.new_comment.comment, 'test comment')
        self.assertEquals(self.new_comment.blog_id,self.new_blog.id)
        self.assertEquals(self.new_comment.user_id,self.user_njiiri)

    def save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()> 0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        g_comment = Comment.get_comment(1)
        self.assertTrue(g_comment is not None)