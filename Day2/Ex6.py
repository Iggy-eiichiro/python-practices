def admin_only(func):
    def wrapper(user):
        if user.get('role') != 'admin':#!= is mean, not equal. User of role is not admin, print("Permission Denied")
            print("Permission Denied")
            return None 

        return func(user)

    return wrapper


@admin_only
def delete_data(user):
    print("Data deleted")


user = {'role': 'guest'}

delete_data(user)