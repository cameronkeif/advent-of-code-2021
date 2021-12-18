depths = File.open("input.txt").readlines.map(&:chomp)

depthIncreases = depths.drop(1).each.with_index(1).reduce(0) do |sum, (depth, i)|
  if (depth.to_i > depths[i - 1].to_i)
    sum += 1
  end
  sum
end

puts(depthIncreases.to_s + " depth increases.")
