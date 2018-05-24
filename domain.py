email = input("Enter your email")
index_at = email.index("@")
username = email[:index_at:]
domain = email[index_at+1::]
print(username)
print(domain)
