"""
       @Author: Habib Ibrahim
       @Date: 27/05/2023
       @issue: Ski rental problem (rent/buy) - Online Algorithms
       @Version: "0.1" , "python 3.12"

Introduction:
    Ski rental problem (rent/buy problem) is a name given to a class of problems in which there is a
    choice between continuing to pay a repeating cost or paying a one-time cost which eliminates or reduces
    the repeating cost.

Motivation:
    Many online problems have a sub-problem called the rent/buy problem. We need to decide whether to stay in
    the current state and pay a certain amount of cost per time unit, or switch to another state and pay some fixed
    large cost with no further payment.

I/O:
    Input:  rent price for a day, buying full-price
    Output: number of the best day to buy , cost user will pay

Example:
    Input: 6$ to rent per day, 30$ buying price
    Output: ' Day number 5 is best day to buy! payment will be 54$.
              You can keep renting until day 4, but in day number 5 you should buy it! '

"""


# Problem input
def ROBInput():
    return int(input('Rent Price Per Day:')), int(input('Buy Price:'))


# calculate price ratio between optimum and user in day k and k + 1.
# if k + 1 is not better than k then k is the day to buy.
def calculatePrices(dayNum, rentPerDay, buyPrice):
    day_k_ratio = float(((dayNum - 1) * rentPerDay + buyPrice) /
                        (dayNum * rentPerDay if dayNum * rentPerDay < buyPrice else buyPrice))

    day_k_plus_1_ratio = float((dayNum * rentPerDay + buyPrice) /
                               ((dayNum + 1) * rentPerDay if (dayNum + 1) * rentPerDay < buyPrice else buyPrice))
    return True if day_k_plus_1_ratio < day_k_ratio else False


# User don't know how many days he will stay, algorithms run until it finds the best day to buy
def calculateBestDayToBuy(rentPerDay, buyPrice):
    day_num = 1
    notDone = 0
    while notDone != 1:
        if calculatePrices(day_num, rentPerDay, buyPrice):
            day_num += 1
        else:
            notDone = 1
            ROBOutput(rentPerDay, buyPrice, day_num)


# Problem Output
def ROBOutput(rentPerDay, buyPrice, bestBuyingDay):
    if bestBuyingDay == 1:
        print("Day number " + str(bestBuyingDay) + " is best day to buy! Payment will be "
              + str((bestBuyingDay - 1) * rentPerDay + buyPrice) + "$\n")
    else:
        print("Day number " + str(bestBuyingDay) + " is best day to buy! Payment will be "
              + str((bestBuyingDay - 1) * rentPerDay + buyPrice) + "$\n"
              + "You can keep renting until day " + str(bestBuyingDay - 1)
              + ", but in day number " + str(bestBuyingDay) + " you should buy it!")


# main
if __name__ == '__main__':
    rent_per_day, buy_price = ROBInput()
    calculateBestDayToBuy(rent_per_day, buy_price)
