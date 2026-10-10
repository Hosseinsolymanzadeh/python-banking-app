def require_role(*role):
    def dicoreator(func):
        def wrapper(*args, **kwargs):
            if args[0] not in user:
                print(f"User {args[0]} does not exist.")
                return
            elif user[args[0]][0] not in role:
                print("Access denied")
                return
            func(*args, **kwargs)    
        return wrapper  
    return dicoreator    


def add_user(user):
    user[(input("enter your name:\n")).lower()] = [(input("Chose your role user/admin/guest:\n")).lower(), int(input("What's your balance:\n"))]
    return user

@require_role("admin")
def delet_user(*args):
    user.pop(args[1])


def view_profile(*args):
    print(f"Profile of {args[0]}\nRole: {args[1]}")

@require_role("admin", "user")
def view_balance(*args):
        print(f"Profile of {args[0]}\nBalance: {user[args[0]][1]}")


@require_role("admin", "user")
def transfer_money(*args):
    if args[0] not in user:
        print(f"User {args[0]} does not exist.")
        return
    elif args[1] not in user:
        print(f"User {args[1]} does not exist.")
        return
    elif args[0] == args[1]:
        print("You cannot transfer money to yourself.")
        return
    else:
        if int(args[2]) > 0:
            if int(user[args[0]][1]) >= int(args[2]):
                user[args[0]][1] = int(user[args[0]][1]) - int(args[2])
                user[args[1]][1] = int(user[args[1]][1]) + int(args[2])
                print(f"Transfer successful\n{args[2]} was transferred from {args[0]}'s account to {args[1]}'s account.")
            else:
                print("Insufficient balance")
                return

        else:
            print("Transfer amount must be greater than zero.")
            return

user = {}
