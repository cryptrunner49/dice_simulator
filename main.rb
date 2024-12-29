def roll_dice
    print "Roll the dice? (y/n): "
    roll = gets.chomp
    
    while roll.downcase == "y" do
        dice1 = rand(1..6)
        dice2 = rand(1..6)

        puts("dice rolled: #{dice1} and #{dice2}")
        
        z=" o";$><<(s=?-*5+"
|#{z[2/~a=(dice1-1)]} #{z[a/3]}|
|"+z[a/5])+z[~a%2]+s.reverse
puts ""

        z=" o";$><<(s=?-*5+"
|#{z[2/~a=(dice2-1)]} #{z[a/3]}|
|"+z[a/5])+z[~a%2]+s.reverse
puts ""

        print "Roll again? (y/n): "
        roll = gets.chomp
    end
end

roll_dice