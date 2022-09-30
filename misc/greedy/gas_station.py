def gas_station(gas, dist):
    n = len(gas)
    current_start_station = None
    current_gas = 0
    current_station = 0

    while current_station < n*2:
        if current_start_station is None:
            current_start_station = current_station
        current_gas += gas[current_station%n]
        print(f"after pumping {gas[current_station%n]} at station {current_station%n}, gas is {current_gas}")
        current_gas -= dist[current_station%n]
        print(f"after traveling {dist[current_station%n]} from station {current_station%n} to {(current_station+1)%n}, gas is {current_gas}")

        if current_gas < 0:
            current_start_station = None
            current_gas = 0
            print(f"--- let us restart from station {(current_station+1)%n}")

        current_station += 1

        if current_start_station is not None and current_station - current_start_station == n:
            return current_start_station % n
        
    return -1

gas =  [1,2,3,4,5]
dist = [3,4,5,1,2]
ret = gas_station(gas, dist)
print(ret)
