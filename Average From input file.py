def main():
    try:
        number=open('umbers.txt','r')
    except IOError:
        print('An error has occured trying to read the file')
    total=0
    count=0
    for line in number:
        try:
            amount=float(line)
            total=amount+total
            count=count+1
            print(f'I read in {count} number(s) Current number is:  {amount:.2f} Total is:  {total:.2f}')
        except ValueError:
            print('Non-numeric data found in the file. Skipping...')
        average=(total)/(count)
        average=float(average)
    number.close()
    print('Average: ',average)
    
main()
