import networkx as nx


# Find all incoming edges to node N
def findIncomingEdges(G, n):
    return G.in_edges(n)


# Find all outgoing edges from node N
def findOutgoingEdges(G, n):
    return G.edges(n)


# Find all neighbor edges of an edge.
# Neighbor edge: a cell-cell edge sharing the same terminal cell with the given edeg.
def findNeighborEdges(u, v, MergeResult, CommunityNumToNodes, CommEdgeColorInfo, bio_flag):

    edges = set()
    ComU, ComV = MergeResult[u], MergeResult[v]
    for tmp in CommEdgeColorInfo[ComU].keys():
        for node in CommEdgeColorInfo[ComU][tmp]:
            if CommEdgeColorInfo[ComU][tmp][node]["Type"] == "Outgoing":
                edges.add((tmp, node))
            else:
                edges.add((node, tmp))

    for tmp in CommEdgeColorInfo[ComV].keys():
        for node in CommEdgeColorInfo[ComV][tmp].keys():
            if CommEdgeColorInfo[ComV][tmp][node]["Type"] == "Outgoing":
                edges.add((tmp, node))
            else:
                edges.add((node, tmp))

    edges.remove((u,v))
    return list(edges)

