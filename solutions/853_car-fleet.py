class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        def calc_time(car: tuple[int, int]) -> float:
            # t = d / v
            return float(target - car[0]) / car[1]

        stack = [calc_time(cars[0])]

        for car in cars[1:]:
            time = calc_time(car)
            if time > stack[-1]:
                stack.append(time)

        return len(stack)
