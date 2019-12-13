import requests

class ApiLogin(object):

    def api_post_login(self,url,username,password,jenkins,login):

        headers = {'Content-Type': 'application/x-www-form-urlencoded'
                   }
        data ={'_username':username,
               'j_password':password,
               'from':jenkins,
               'Submit':login}

        return requests.session().post(url,headers=headers,data=data)
