uefa_euro_2016 = lambda teams, scores: f"At match {teams[0]} - {teams[1]}, {'teams played draw.' if scores[0] == scores[1] else teams[scores.index(max(scores))] + ' won!'}"

def uefa_euro_2016(teams, scores):
  if scores[0] == scores[1]:
    return f"At match {teams[0]} - {teams[1]}, teams played draw."
  else:
    highest_score = max(scores)
    winner_index = scores.index(highest_score)
    winner_team = teams[winner_index]
    return f"At match {teams[0]} - {teams[1]}, {winner_team} won!"
  
