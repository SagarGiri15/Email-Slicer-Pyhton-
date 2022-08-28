email = input("Enter your Email Address:").strip()

user_name = email[:email.index("@")]

domain_name = email[email.index("@")+1:]

result = "Your Username is '{}' and your domain name is '{}' ".format(user_name,domain_name)

print(result)
