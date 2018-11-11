hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
total_price = 0
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

for i in prices:
  total_price += i
average_price = total_price/len(prices)
print ("Average Haircut Price:")
print (average_price)

new_prices = [j - 5 for j in prices]
print (new_prices)

total_revenue= 0
for i in range(len(hairstyles)): 
  total_revenue += prices[i] * last_week[i]
print ("Total Revenue:")
print (total_revenue)
average_daily_revenue = total_revenue / 7
cuts_under_30 = [
hairstyles[k] 
for k in range(0, len(hairstyles) - 1) 
if new_prices[k]<30
]
print (cuts_under_30)



