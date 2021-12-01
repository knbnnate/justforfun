
def removeIslands(matrix):
  def east(h):
    return h+1 if h+1 < len(matrix[0]) else None
  def north(v):
    return None if  v == 0 else v-1
  def west(h):
    return None if h == 0 else h-1
  def south(v):
    return v+1 if v+1 < len(matrix) else None
  memo = [[None for j in range(len(matrix[0]))] for i in range(len(matrix))]
  def memoize(v,h):
    if matrix[v][h] == 0:
      memo[v][h] = False
    else:
      if east(h) is None or north(v) is None or west(h) is None or south(v) is None:
        memo[v][h] = True
      elif memo[v][east(h)] or memo[north(v)][h] or memo[v][west(h)] or memo[south(v)][h]:
        memo[v][h] = True
      else:
        result = False
        memo[v][h] = result
        if memo[v][east(h)] is None:
          result = result or memoize(v,east(h))
        if memo[north(v)][h] is None:
          result = result or memoize(north(v),h)
        if memo[v][west(h)] is None:
          result = result or memoize(v,west(h))
        if memo[south(v)][h] is None:
          result = result or memoize(south(v),h)
        memo[v][h] = result
    return memo[v][h]
  for v in range(len(matrix)):
    for h in range(len(matrix[0])):
      memoize(v,h)
  return [ [1 if memo[v][h] else 0 for h in range(len(matrix[0]))] for v in range(len(matrix))]

test_matrix = [
  [0,1,0,1,0,1],
  [0,1,0,1,0,1],
  [0,0,1,0,1,0],
  [0,1,1,0,1,0],
  [0,1,1,0,1,0],
  [0,1,0,0,0,1]
]
test_output = removeIslands(test_matrix)
for row in test_output:
  print(row)