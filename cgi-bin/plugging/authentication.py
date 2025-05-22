class Authentication:

    def auth(self,auth_header):
        if auth_header=="seccode":
            return True
        else:
            return False 