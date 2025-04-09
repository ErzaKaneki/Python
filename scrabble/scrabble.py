letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letter_to_points = dict(zip(letters, points))

def score_word(word):
  word = word.upper()
  point_total = 0
  for char in word:
    if char in letter_to_points:
      point_total += letter_to_points.get(char)
  return point_total

print(score_word("brownie"))

player_to_words = {'player1': ['blue', 'tennis', 'exit'], 'wordNerd': ['earth', 'eyes', 'machine'], 'Lexi Con': ['eraser', 'belly', 'husky'], 'Prof Reader': ['zap', 'coma', 'period']}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)