import networkx as nx
import mbuild as mb
import typing


def gen_smarts(node : mb.compound.Compound, 
               G : nx.Graph, depth: int, 
               node_trees: typing.Dict[mb.compound.Compound, nx.classes.digraph.DiGraph]):
    """
    The dynamic programming algorithm to generate SMARTS string for a node in a graph.

    Parameters
    ----------
    node : mb.compound.Compound
        The node to generate the SMARTS string for.
    G : nx.Graph
        The graph to generate the SMARTS string for.
    depth : int
        The depth to traverse in G from node using a breadth first search.
    """
    if depth == 1:
        smarts = '[{};X{}]'.format(node.element.symbol, len(list(G.neighbors(node))))
        for neigh in G.neighbors(node):
            smarts += '({})'.format(neigh.element.symbol)
        return smarts
    smarts = '[{};X{}]'.format(node.element.symbol, len(list(G.neighbors(node))))
    for neigh in G.neighbors(node):
        smarts += '({})'.format(gen_smarts(neigh, G, depth-1, node_trees))
    return smarts

def bond_graph_to_smarts_dic(BG, depth=1):
    """
    Generates a dictionary of SMARTS strings for each node in a bond graph.
    
    Parameters
    ----------
    BG : nx.Graph
        The bond graph to generate the SMARTS strings for.
    depth : int
        The depth to traverse in BG from node using a breadth first search.
    """
    G = nx.Graph(BG._adj)
    smarts_dic = {}
    node_to_tree = {n:nx.bfs_tree(G, n) for n in G.nodes}
    for c_node in G.nodes():
        smarts_dic[c_node] = gen_smarts(c_node, G, depth, node_to_tree)
    return smarts_dic