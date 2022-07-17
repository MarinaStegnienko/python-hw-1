s=input("Введіть рядок: ")
t=s[:5]
print(t,'...')
s1=s.capitalize()
s2=s.lower()
if s[0]=='L':
    print(s2)
else:
    if s[0]=='l':
       print(s1)
    else:
        if s[0]=='U':
            print(s2)
        else:
            if s[0]=='u':
                print(s1)



