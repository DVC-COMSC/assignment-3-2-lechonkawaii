[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10512549)
<email = input('enter your string')

flag = True
if not email[0].isalpha():
     flag - False
lenemail = len(email)
if lenemail <= 5 or lenemail >= 30:
      flag = False
if email.find('@') == -1:
    flag = False
else: 
     atidx = email.find('@') 
if email[atidx+1].find('.') == -1:
    flag = False

print (flag)

if __name__ == '__main__':
    main()!--

## Complete the "main.py"
