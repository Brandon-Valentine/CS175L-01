def book_list():
    book=[]
    books=open('bestsellers.txt','r')
    count=0

    for line in books:
        l=line.strip('\n')
        cols=l.split('\t')
        book.append(cols)
        count+=1
    print(count)
    print(book[1137][3])
    date = book[1137] [3].split('/')
    print(date)                            
    s=input('Enter the title.')
    #s=input('Enter the author')
    s=s.lower()
    #=t.lower()


    for entry in book:
        t=entry[0].lower()
        #print(t)
        if t.find(s)!=-1:
            print(t)


            
            
        books.close()
book_list()




def menu():
    print(f'Read 1138 books')

    print('1: Look up year range')
    print('2: Look up month/year')
    print('3: Search for Author')
    print('4: Search for title')
    print('Q: Quit')
    choice=input('What would you like to do?')

def option_1(book_list):
    start_year=int(input('Enter a starting year: '))
    end_year=int(input('Enter an ending year: '))
    copies[start_year : end_year]

#def main():
    
    




    
