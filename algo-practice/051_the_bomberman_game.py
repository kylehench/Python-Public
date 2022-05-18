def bomberMan(n, grid):
  grid = [[3 if t=='O' else '.' for t in s] for s in grid]
  

test = (3, ['.......','...O...','....O..','.......','OO.....','OO.....'])
print(bomberMan(*test))