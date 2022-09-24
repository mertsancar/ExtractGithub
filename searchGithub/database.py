import psycopg2

from searchGithub.models import Candidate

def add_candidate_toDB(user):

    if not is_exist(user["userLink"]):
        candidate = Candidate()
        candidate.username = user["username"]
        candidate.title = user["title"]
        candidate.userLink = user["userLink"]
        candidate.description = user["description"]
        candidate.country = user["country"]

        candidate.save_base()

def get_github_candidates(keyword):
    
    conn = psycopg2.connect(
    database="myDB", user='postgres', password='123', host='127.0.0.1', port= '5432'
    )

    #Setting auto commit false
    # conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Retrieving data
    # cursor.execute('''SELECT * FROM public."searchGithub_candidate" WHERE ORDER BY id ASC ''')
    cursor.execute('''SELECT * FROM public."searchGithub_candidate" WHERE "title" = '{}' ORDER BY id ASC  '''.format(keyword))

    result = cursor.fetchall()

    #Closing the connection
    conn.close()

    candidates = list()
    for user in result:

        candidates.append({"username":user[1],
                           "title":user[2],
                           "description": user[3],
                           "country": user[4],
                           "userLink":user[5]})
                    
    #Commit your changes in the database
    # conn.commit()   

    return candidates

def is_exist(userLink):
    
    conn = psycopg2.connect(
    database="myDB", user='postgres', password='123', host='127.0.0.1', port= '5432'
    )

    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM public."searchGithub_candidate" WHERE "userLink" = '{}' LIMIT 1  '''.format(userLink))

    result = cursor.fetchall()

    conn.close()

    if len(result) >= 1:
        return True
    else:
        return False
                    