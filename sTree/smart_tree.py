import networkx as nx
import mbuild as mb
import typing


def gen_smarts(node : mb.compound.Compound, 
               G : nx.Graph, depth: int, 
               node_trees: typing.Dict[mb.compound.Compound, nx.classes.digraph.DiGraph]):
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
    G = nx.Graph(BG._adj)
    smarts_dic = {}
    node_to_tree = {n:nx.bfs_tree(G, n) for n in G.nodes}
    for c_node in G.nodes():
        smarts_dic[c_node] = gen_smarts(c_node, G, depth, node_to_tree)
    return smarts_dic