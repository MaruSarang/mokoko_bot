def calculate_from_user(user, max=1):  # 3을 지정하지 않으면 기본값이 1로 나옴

def print_users_sum():
    sum = 0
    if user != "test":
        return None

    while sum < max:
        sum = sum + 1
        print(sum)


sum = 0
user = input()
calculate_from_user(user, 3)  # 3을 지정하면 3까지 나옴
calculate_from_user("test")  # 기존 사용방식