class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position,speed),key=lambda car: car[0], reverse=True)
        car_fleets = [(target - sorted_cars[0][0])/sorted_cars[0][1]]
        for i in range(1, len(sorted_cars)):
            time = (target-sorted_cars[i][0])/sorted_cars[i][1]
            if time > car_fleets[-1]:
                car_fleets.append(time)
        return len(car_fleets)