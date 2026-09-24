class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = []
        for i in range(len(position)):
            space_left = target - position[i]
            timestep = (space_left/speed[i])
            tuples.append((position[i],timestep))
        tuples.sort(reverse=True)
        stack = []
        for p,timestep in tuples:
            if not stack:
                stack.append(timestep)
            else:
                if timestep > stack[-1]:
                    stack.append(timestep)

        return len(stack)

        