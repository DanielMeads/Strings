# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

"""Reporting on the 1988 UEFA final"""

# Players that scored and time
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
player = "Ronald Koeman"
first_name = player[  : int(player.find(" ",0,len(player)))]
last_name_len = len(player[int(player.find(" ",0,len(player))):len(player)])-1
name_short = f"{player[0:1]}. {player[-last_name_len:len(player)]}"
chant = ((first_name + "! " ) * len(first_name))[:-1]
good_chant = chant[-1] != " "
scorers = f"{scorer_0} {str(goal_0)}, {scorer_1} {str(goal_1)}"

report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"

print (report)
print (last_name_len)
print (good_chant)
print (scorers)
print (name_short)
print (chant)