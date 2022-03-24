def main():
    number=open('numbers.txt','r')
    total=0
    count=0
    for line in number:
        amount=float(line)
        total=amount+total
        total=float(total)
        count=count+1
        print(f'I read in {count} number(s) Current number is:  {amount:.2f} Total is:  {total:.2f}')
        average=(total)/(count)
        average=float(average)
    number.close()
    print('Average: ',average)
main()
