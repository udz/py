# calculate profit or loss percentage depending upon selling and cost price

def percentage(sp,cp):
    selling_price = int(sp)
    cost_price = int(cp)
    if selling_price > cost_price:
        profit_percent = {}
        profit_percent['profit %'] = (selling_price - cost_price)/cost_price * 100
        return profit_percent
    elif selling_price < cost_price:
        loss_percent = {}
        loss_percent['loss %'] = (cost_price - selling_price)/cost_price * 100
        return loss_percent
    else:
        equal = {}
        equal['equal'] = 0
        return equal

print(percentage(100,200))
print(percentage(100,100))
print(percentage(200,100))