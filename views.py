from blog.models import users,posts
# print(users)

# username="Akhil"
# password="Password@123"
# user=[user for user in users if user["username"]==username and user["password"]==password]
# if user:
#     print("success")
# else:
#     print("failed")

session={}
def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("Invalid session U mut login")
    return wrapper




def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user
# print(authenticate(username="akhil",password="Password@123"))

class LoginView:
    def post(self,*args,**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
        print(session)




class PostlistView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts



log_in=LoginView()
log_in.post(username="akhil",password="Password@123")
all_post=PostlistView()
print(all_post.get())


