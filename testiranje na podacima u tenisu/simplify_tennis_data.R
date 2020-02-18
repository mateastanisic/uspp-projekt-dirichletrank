scores2017 = read.csv( "match_scores_2017_unindexed_csv.csv" )

n = length(scores2017[,1])

players = levels(scores2017$Loser_Name)
winners = levels(scores2017$Winner_Name)
for( winner in winners )
  if( !(winner %in% players) )
    players = c( players, winner )
players = sort(players)

nplayers = length(players)

matches2017 = matrix( 0, nrow = n, ncol = 6 )
colnames(matches2017) = c( "winner", "loser", "winner_sets_won", "loser_sets_won", "winner_games_won", "loser_games_won" )
for( i in 1:n  )
{
  winner = scores2017[i,"Winner_Name"]
  loser  = scores2017[i,"Loser_Name"]
  
  for( j in 1:nplayers )
  {
    if( players[j] == winner )
    {
      matches2017[i,1] = j
      matches2017[i,3] = scores2017[i,"winner_sets_won"]
      matches2017[i,5] = scores2017[i,"winner_games_won"]
    }
    if( players[j] == loser )
    {
      matches2017[i,2]  = j
      matches2017[i,4] = scores2017[i,"loser_sets_won"]
      matches2017[i,6] = scores2017[i,"loser_games_won"]
    }
  }
}

write.table( players, "tennis_players_alphabetically_2017.txt", sep="\n", row.names = F, col.names = F )
write.table( matches2017, "tennis_matches_2017.txt", row.names = F, col.names = F )

atpRank = read.csv2( "atp_rank_2017.csv", header=T )
playersRanked = c()
for( i in 1:2000  )
{
  player = as.character( atpRank$player[i] )
  for( j in 1:nplayers )
    if( players[j] == player )
    {
      playersRanked = c( playersRanked, j )
      break
    }
}

for( i in 1:nplayers )
  if( !( i %in% playersRanked ) )
    playersRanked = c( playersRanked, i )

write.table( playersRanked, "tennis_players_ranked_atp_2017.txt", sep="\n", row.names = F, col.names = F )
