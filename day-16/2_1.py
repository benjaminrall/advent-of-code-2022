from parse import compile
with open("input.txt", "r") as f:
    inp = f.read()
pat = compile("Valve {} has flow rate={:d}; tunnels lead to valves {}")

ans1 = 0
to_node = {}
idx = {}
class Node:
	def __init__(self, flow, tunnels):
		self.flow = flow
		self.tunnels = tunnels
		self.opened = False

nnodes = 0
nspecial = 0
vs = []
for s in inp.split("\n"):
    print(s)
    valve, flow, tt = pat.parse(s)
    to_node[valve] = Node(flow, tt.split(", "))
    if flow > 0:
        nspecial += 1
    vs.append(valve)
    nnodes += 1
vs = sorted(vs, key=lambda x: to_node[x].flow, reverse=True)
flow = []
idx = {}
for i, v in enumerate(vs):
    idx[v] = i

dist = {}
for i in range(nnodes):
    for j in range(nnodes):
    	dist[i,j] = 1 << 30

for i in range(nnodes):
    flow.append(to_node[vs[i]].flow)
    for b in to_node[vs[i]].tunnels:
    	dist[i,idx[b]] = 1

for k in range(nnodes):
    for i in range(nnodes):
    	for j in range(nnodes):
    		dist[i,j] = min(dist[i,j], dist[i,k] + dist[k,j])

dp = {}
def solve_mask(cur_node, time, cur_mask):
    global dp
    key = (cur_node, time, cur_mask)
    if key in dp:
        return dp[key]
    ans = 0
    for i in range(nspecial):
        if ((cur_mask >> i) & 1) == 1:
            ntime = time - dist[cur_node, i] - 1
            if ntime > 0:
                ans = max(ans, solve_mask(i, ntime, cur_mask ^ (1 << i)) + flow[i] * ntime)
    dp[key] = ans
    return ans

res = 0
for msk in range(1 << (nspecial - 1)):
	res = max(res, solve_mask(idx["AA"], 26, msk) + solve_mask(idx["AA"], 26, msk ^ ((1 << nspecial) - 1)))
print(res)