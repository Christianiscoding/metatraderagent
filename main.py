import MetaTrader5 as mt5
import credentials
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()
mt5.login(login = credentials.username, password=credentials.password)
 
# check the presence of active orders
orders=mt5.orders_total()
if orders>0:
    print("Total orders=",orders)
else:
    print("Orders not found")

# display data on active orders on GBPUSD
orders=mt5.orders_get(symbol="EURAUD")
if orders is None:
    print("No orders on GBPUSD, error code={}".format(mt5.last_error()))
else:
    print("Total orders on GBPUSD:",len(orders))
    # display all active orders
    for order in orders:
        print(order)
print()

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()