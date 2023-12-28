# ROBAlgorithm
       @Author: Habib Ibrahim
       @Date: 27/05/2023
       @issue: Ski rental problem (rent/buy) - Online Algorithms
       @Version: "0.1" , "python 3.12"
code can be executed at: https://colab.research.google.com/drive/1njoJsXlWyZihBw0c_2obxNynkFK7hSGe?usp=sharing

Introduction:

        Ski rental problem (rent/buy problem) is a name given to a class of problems in which there is a
        choice between continuing to pay a repeating cost or paying a one-time cost which eliminates or reduces
        the repeating cost.

Motivation:

       Many online problems have a sub-problem called the rent/buy problem. We need to decide whether to stay in
       the current state and pay a certain amount of cost per time unit, or switch to another state and pay some 
       fixed large cost with no further payment.

I/O:

    Input:  rent price for a day, buying full-price
    Output: number of the best day to buy , cost user will pay

Example:

    Input: 6$ to rent per day, 30$ buying price
    Output: ' Day number 5 is best day to buy! payment will be 54$.
              You can keep renting until day 4, but in day number 5 you should buy it! '
