players = importdata('tennis_players_alphabetically_2017.txt');
matches = importdata('tennis_matches_2017.txt');
atplist = importdata('tennis_players_ranked_atp_2017.txt');

n = size(players,1);
G = zeros(n,n);
nmatches = size( matches, 1 );
for( i = 1:nmatches )
    winner = matches(i,1);
    loser  = matches(i,2);
    
    % brojimo osvojene gemove
    G( winner, loser ) = G( winner, loser ) + matches(i,5);
    G( loser, winner ) = G( loser, winner ) + matches(i,6);
end;

eps = 10^(-10);
A = zeros(n,n);
for( j = 1:n )
    nj = sum(G(:,j));
    if( nj > 0 )
        A(:,j) = G(:,j) / nj;
    end;
end;


%%%%% Page Rank

alpha = 0.85;
S = 1/n * ones(n,n);
M = alpha * A + (1-alpha) * S;

x = rand(n,1);
x = x / sum(x);

max_it = 1000;
d = zeros(max_it);

nit = 1;
Mx = alpha * A * x + (1-alpha)/n * ones(n,1) * sum(x);
new_x = Mx / sum(Mx);
d(1) = norm(x - new_x);
while( d(nit) >= eps && nit <= max_it  )
    Mx = alpha * A * x + (1-alpha)/n * ones(n,1) * sum(x);
    new_x = Mx / sum(Mx);
    nit = nit + 1;
    d(nit) = norm( x - new_x );
    x = new_x;
end;

nit
[B,I] = sort(x,'descend');

y = zeros(n,1);
for( i = 1:n )
  for( j = 1:n )
    if( I(j) == atplist(i) )
      y(i) = j;
      break;
    end;
  end;
end;

PRgames = I;
figure(1);
newplot();
hold on
plot( y(1:490), 'o', 'color', 'm' ); % igraci iza 491. mjesta nemaju niti jednu pobjedu
plot( 1:490 );
corr( 1:490, y(1:490) )
corr( 1:100, y(1:100) )

PRgames_y = y;

%{

%%%%% Dirichlet Rank

mu = 10;
omega = zeros(n,1);
for( i = 1:n )
  omega(i) = mu / ( sum(G(i,:)) + mu );
end;
U = 1/n * ones(n,n);
M = diag(1-omega) * A + diag(omega) * U;

%}