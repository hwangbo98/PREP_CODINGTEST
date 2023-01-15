class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_box = 0
        cost = 0
        boxTypes.sort(key=lambda x : (-x[1], -x[0]))
        print(boxTypes)
        
        for k, box in enumerate(boxTypes) :
            total_box += box[0]
            if(total_box > truckSize) :
                total_box -= box[0]
                cost+= (truckSize - total_box) * box[1]
                print(f'total_box is {total_box} cost is {cost}')
                break
            else :
                cost+= box[0] * box[1]
                print(f'total_box is {total_box} cost is {cost}')


        return cost