def tournament_winner(competitions, scores):
    current_best = ''
    scores_map = {current_best: 0}
    for i, competition in enumerate(competitions):
        result = result[i]
        home_team, away_team = competition
        winner = home_team if result == 1 else away_team
        if winner not in scores_map:
            scores_map[winner] = 0
        scores_map[winner] += 3
        if scores_map[winner] > scores_map[current_best]:
            current_best = winner
    return current_best