def check_user_exists(username):
    if username not in user:
        print(f"User {username} does not exist.")
        return False
    return True

def check_role(username, *role):
    if user[username][0] not in role:
        print(f"User {username} does not have the required role: {role}.")
        return False
    return True

def check_sufficient_balance(username, amount):
    if user[username][1] < amount:
        print("Insufficient balance")
        return False
    return True

def check_transfer_amount(amount):
    if amount <= 0:
        print("Transfer amount must be greater than zero.")
        return False
    return True

def require_role(*role):
    def dicoreator(func):
        def wrapper(*args, **kwargs):
            if check_user_exists(args[0]) and check_role(args[0], *role):
                return func(*args, **kwargs)    
        return wrapper  
    return dicoreator    

def add_user(user):
   user_id = generator_id()
   info = get_info()
   user[user_id] = info  
   print(f"""****************************
   User {user_id} added successfully.
   ****************************
   Username: {info['username']}
   Role: {info['role']}
   Email: {info['email']}
   Phone: {info['phone']}
   ****************************""")
def view_profile(*args):
    print(f"Profile of {args[0]}\nRole: {args[1]}")

@require_role("admin")
def delet_user(*args):
    user.pop(args[1])

@require_role("admin", "user")
def view_balance(*args):
        print(f"Profile of {args[0]}\nBalance: {user[args[0]][1]}")

@require_role("admin", "user")
def transfer_money(*args):
        
    if args[0] == args[1]:
        print("You cannot transfer money to yourself.")
        return
    else:
        if check_user_exists(args[1]) and check_transfer_amount(int(args[2])) and check_sufficient_balance(args[0], int(args[2])):
            user[args[0]][1] = int(user[args[0]][1]) - int(args[2])
            user[args[1]][1] = int(user[args[1]][1]) + int(args[2])
            print(f"Transfer successful\n{args[2]} was transferred from {args[0]}'s account to {args[1]}'s account.")


def generator_id():
    user_ids = [int(uid) for uid in user.keys()]
    return max(user_ids) + 1 if user_ids else 1

user ={}
def get_info():
    username = input("Enter your username:\n").lower()
    password = input("Enter your password:\n")
    role = input("Chose your role user/admin/guest:\n").lower()
    email = input("Enter your email:\n")
    phone = input("Enter your phone number:\n")
    return {
        "username": username,
        "password": password,
        "role": role,
        "email": email,
        "phone": phone
    }

