depths = File.open("input.txt").readlines.map(&:chomp)

depthIncreases = depths.drop(3).each.with_index(3).reduce(0) do |sum, (depth, i)|
  previousWindow = depths[i - 1].to_i + depths[i - 2].to_i + depths[i - 3].to_i
  currentWindow = depth.to_i + depths[i - 1].to_i + depths[i - 2].to_i
  
  if(currentWindow > previousWindow)
    sum += 1
  end

  sum
end

puts(depthIncreases.to_s + " depth increases.")
