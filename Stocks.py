#CS175L-01
#BrandonValentine
#Stocks



COMMISSION_RATE=float(input('What was the commission rate?: '))
NUM_SHARES=int(input('How many shares did you purchase?: '))
PURCHASE_PRICE=float(input('What was the purchase price?: '))
SELLING_PRICE=float(input('What was the selling price?:' ))
amountPaidForStock=NUM_SHARES*PURCHASE_PRICE
purchaseCommission=COMMISSION_RATE*amountPaidForStock
totalPaid=amountPaidForStock+purchaseCommission
stockSoldFor=NUM_SHARES*SELLING_PRICE
sellingCommission=COMMISSION_RATE*stockSoldFor
totalRecieved=stockSoldFor-sellingCommission
profitOrLoss=totalRecieved-totalPaid
totalCommission=sellingCommission+purchaseCommission
print(f'Amount paid for stock: $ {amountPaidForStock}')
print(f'Commission paid on the purchase: $ {purchaseCommission}')
print(f'Amount the stock sold for: $ {stockSoldFor}')
print(f'Commission paid on the sale: $ {sellingCommission}')
print(f'Total commission paid: $ {totalCommission}')
print(f'Profit(or loss if negative): $ {profitOrLoss}')
