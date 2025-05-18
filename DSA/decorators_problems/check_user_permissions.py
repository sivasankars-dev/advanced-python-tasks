# Build a @require_admin decorator that simulates permission-checking:
# Assume current_user = {"is_admin": False} and block execution unless is_admin == True.
auth_users = {100,102,103}
def require_admin(fn):
    current_user = {}
    def wrapper(userId):
        if userId in current_user:
            exists = current_user['is_admin']
        else:
            exists = userId in auth_users
            current_user['is_admin'] = exists

        if not exists:
            print(f'{userId} is not exists')
            return None
        
        return fn(userId)

    return wrapper

@require_admin
def callFn(userId):
    print(f"Existing userid {userId}")

callFn(100)
callFn(102)
callFn(100)