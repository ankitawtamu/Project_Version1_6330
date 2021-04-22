import unittest
import sqlite3
from unittest import result, mock

from flask.templating import render_template
import main



con = sqlite3.connect('./flaskr/db.sqlite')
cur = con.cursor()

class TestMain(unittest.TestCase):

    #Test route for home page 
    def test_index(self):
        tester = main.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Lodge Complaint and Provide Feedback', response.data)

    #Test route for dashboard page 
    def test_dashboard(self):
        tester = main.test_client(self)
        response = tester.get('/dashboard')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Dashboard', response.data)

         #Test route for service page 
    def test_service(self):
        tester = main.test_client(self)
        response = tester.get('/service')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Service', response.data)


      #Test route for complaint page 
    def test_complaint(self):
        tester = main.test_client(self)
        response = tester.get('/complaint')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Complaint', response.data)


    # Testing delete page route
    def test_delete(self):
        tester = main.test_client(self)
        response = tester.get('/delete')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Delete Complaint', response.data)

        # Testing update page route
    def test_update(self):
        tester = main.test_client(self)
        response = tester.get('/update')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Update Complaint', response.data)

     # Test the presesnce of record in database with select statement 
    def select(self):


        '''cur.execute("select * from Store where id = 2")
        x = cur.fetchone()
        assert x == (2,'tablet not working','walmart')'''

# Testing orderby from database
    def orderby(self):

       ''' row = cur.execute('SELECT * FROM Store ORDER BY type')
        result_list = row.fetchone()
        assert result_list == (4, 'Earphone is faulty', 'kroger')

'''
        

if __name__ == "__main__":
    unittest.main()