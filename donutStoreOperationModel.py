#DONUT STORE SIMULATION
import scipy.stats

demand = 1000 #demand per day
workerOutput = 20 #worker output per hour
rawCostPerDonut = 0.5 #raw cost per donut
revenuePerDonut = 3 #revenue per donut
workerSalary = 10 #worker salary per hour

demandMean= 1000
demandStd = 250

def calcProfitPerDay(workers):
    grossProfitPerUnit = (revenuePerDonut - rawCostPerDonut)
    productionFlowRate = workerOutput*8*workers
    UnitsSold = min(demand, productionFlowRate) #the amount of donuts we can sell is capped by demand
    laborCost = workerSalary*8*workers

    profit = profitPerUnit*UnitsSold - laborCost

    return profit

def calcProfitPerDayVariability(workers):

    grossProfitPerUnit = (revenuePerDonut - rawCostPerDonut)    
    productionFlowRate = workerOutput*8*workers
    laborCost = workerSalary*8*workers

    #incorperates variability into the units sold
    demandDist = scipy.stats.norm(demandMean, demandStd) #mean, std
    profit = 0
    for currentDemand in range(demandMean-4*demandStd, demandMean+4*demandStd + 1):
        UnitsSold = min(currentDemand, productionFlowRate) #the amount of donuts we can sell is capped by demand

        prob = demandDist.pdf(currentDemand) #probability of this demand number occuring based on the probability density function

        profit += prob*(grossProfitPerUnit*UnitsSold - laborCost) #adds the profit for a specific demand level on a probability adjusted basis to total profits

    return profit

#results without variability
print('\nresults without variability\n')
optimalWorkers = 0
optimalProfit = 0
for currentWorkers in range(0, 16):
    currentProfit = calcProfitPerDay(currentWorkers)
    print(currentWorkers, currentProfit)
    if currentProfit>optimalProfit:
        optimalWorkers = currentWorkers
        optimalProfit = currentProfit

print('optimal workers:', optimalWorkers)
print('optimal profit:', optimalProfit)

#results with variability
print('\nresults with variability\n')
optimalWorkers = 0
optimalProfit = 0
for currentWorkers in range(0, 16):
    currentProfit = calcProfitPerDayVariability(currentWorkers)
    print(currentWorkers, currentProfit)
    if currentProfit>optimalProfit:
        optimalWorkers = currentWorkers
        optimalProfit = currentProfit

print('optimal workers:', optimalWorkers)
print('optimal profit:', optimalProfit)
        

