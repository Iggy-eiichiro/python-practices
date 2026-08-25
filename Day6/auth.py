import jwt


SECRET_KEY = "my-secret-key"# for learning. basically do not write like that.
#import os SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"# when i make jwt, use this ALGORITHM


def create_access_token(user_id: int):

    data = {
        "sub": str(user_id)# sub = subject
    }

    token = jwt.encode( # jwt make jwt encode, and put into token
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token