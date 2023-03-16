def main():
    ##################################################
    # Comlete your code here
    ##################################################
    email = input('Enter your email: ')
    
    if(email[0].isalpha()):
       if(len(email) > 5 or len(email) < 30):
         if(email.find('@')):
           if('.' in email):
              print('true')
           else:
               print('false')
         else:
              print('false')
       else:
           print('false')
    else:
        print('false')
    pass


if __name__ == '__main__':
    main()
