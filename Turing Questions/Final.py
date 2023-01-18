""""
    In order to solve this problem, I keep track of each value's membership in group "a"
    or group "b" of the game during each round, and I concatenate the outcome as a string 
    with respect to each value's index value in a separate list using the index as a key. 
    The length of the set of the list and the length of the list itself can be compared to 
    see if there are any repeated values. If a string appears more than once, it indicates 
    that indices with the same string value haven't been played against. This method is more
    effective because of its O(m*n) time complexity.
"""

def solution(n:int , m: int , k) -> bool:
    #write your solution here
    # assign each player an empty string
    team = ['' for i in range(n)]
    # get the half of the total round players
    half = n//2
    # Iterate through each round
    for i in range(m):
        # Iterate through each player in the round
        for j in range(n):
            # Identify each player using their index
            player = k[i][j]
            # group the rivals into group 'a' if their index is less than half of the total round playres and group 'b' otherwise
            if j < half:
                # since player is an index of the player in Natual numbers, we subtract 1 to get the correct index
                team[player-1] += 'a'
            else:
                # since player is an index of the player in Natual numbers, we subtract 1 to get the correct index
                team[player-1] += 'b'
    # By determining whether the string has a repeated value using the set of the list with the list itself, you may assign validity of the response to the "All played" variable.
    Allplayed = len(team) == len(set(team))
    return Allplayed