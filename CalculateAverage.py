#CS 175-01
#Brandon Valentine
#Grade average assignment

def calc_average():
    score1=int(input('Enter score 1: '))
    score2=int(input('Enter score 2: '))
    score3=int(input('Enter score 3: '))
    score4=int(input('Enter score 4: '))
    score5=int(input('Enter score 5: '))
    return score1,score2,score3,score4,score5

def determine_grade(ts1,ts2,ts3,ts4,ts5):
    avg=(ts1+ts2+ts3+ts4+ts5)/5
    if ts1>=90:
        print(f'Score 1:  {ts1:>14.1f}\t    A')
    elif ts1>=80 and ts1<90:
        print(f'Score 1:  {ts1:>14.1f}\t    B')
    elif ts1>=70 and ts1<80:
        print(f'Score 1:  {ts1:>14.1f}\t    C')
    elif ts1>=60 and ts1<70:
        print(f'Score 1:  {ts1:>14.1f}\t    D')
    else:
        print(f'Score 1:  {ts1:>14.1f}\t    F')
    if ts2>=90:
        print(f'Score 2:  {ts2:>14.1f}\t    A')
    elif ts2>=80 and ts2<90:
        print(f'Score 2:  {ts2:>14.1f}\t    B')
    elif ts2>=70 and ts2<80:
        print(f'Score 2:  {ts2:>14.1f}\t    C')
    elif ts2>=60 and ts2<70:
        print(f'Score 2:  {ts2:>14.1f}\t    D')
    else:
        print(f'Score 2:  {ts2:>14.1f}\t    F')
    if ts3>=90:
        print(f'Score 3:  {ts3:>14.1f}\t    A')
    elif ts3>=80 and ts3<90:
        print(f'Score 3:  {ts3:>14.1f}\t    B')
    elif ts3>=70 and ts3<80:
        print(f'Score 3:  {ts3:>14.1f}\t    C')
    elif ts3>=60 and ts3<70:
        print(f'Score 3:  {ts3:>14.1f}\t    D')
    else:
        print(f'Score 3:  {ts3:>14.1f}\t    F')
    if ts4>=90:
        print(f'Score 4:  {ts4:>14.1f}\t    A')
    elif ts4>=80 and ts4<90:
        print(f'Score 4:  {ts4:>14.1f}\t    B')
    elif ts4>=70 and ts4<80:
        print(f'Score 4:  {ts4:>14.1f}\t    C')
    elif ts4>=60 and ts4<70:
        print(f'Score 4:  {ts4:>14.1f}\t    D')
    else:
        print(f'Score 4:  {ts4:>14.1f}\t    F')
    if ts5>=90:
        print(f'Score 5:  {ts5:>14.1f}\t    A')
    elif ts5>=80 and ts5<90:
        print(f'Score 5:  {ts5:>14.1f}\t    B')
    elif ts5>=70 and ts5<80:
        print(f'Score 5:  {ts5:>14.1f}\t    C')
    elif ts5>=60 and ts5<70:
        print(f'Score 5:  {ts5:>14.1f}\t    D')
    else:
        print(f'Score 5:  {ts5:>14.1f}\t    F')
    if avg>=90:
        print(f'Average Score: {avg:>9.1f}\t    A')
    elif avg>=80 and avg<90:
        print(f'Average Score: {avg:>9.1f}\t    B')
    elif avg>=70 and avg<80:
        print(f'Average Score: {avg:>9.1f}\t    C')
    elif avg>=60 and avg<70:
        print(f'Average Score: {avg:>9.1f}\t    D')
    else:
        print(f'Average Score: {avg:>9.1f}\t    F')
        
        

    



def main():
    ts1,ts2,ts3,ts4,ts5 =calc_average()
    score=('Score')
    num_grade=('Numeric Grade')
    let_grade=('Letter Grade')
    print(f'{score}{num_grade:>23}  {let_grade}')
    print('----------------------------------------------------')
    determine_grade(ts1,ts2,ts3,ts4,ts5)

main()
