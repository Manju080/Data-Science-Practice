from winreg import ExpandEnvironmentStrings


class Graphs:
    def __init__(self,edges) -> None:
        self.edges=edges
        self.graph_dic={}
        for start ,end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start]=[end]
        print(self.graph_dic)
    def ge_paths(self,start,end,path=[]):
        path=path +[start]
        if start==end:
            return[path]
        if start not in self.graph_dic:
            return []
        paths=[]
        for node in self.graph_dic:
            if node not in path:
                new_path = self.ge_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
    def shortest_path(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return path        
        if start not in self.graph_dic:
            return None
        short_path=None
        for node in self.graph_dic:
            if node not in path:
                sp=self.shortest_path(node,end,path)
                if sp:
                    if short_path is None or len(sp)<len(short_path):
                        short_path=sp
        return short_path




if __name__=='__main__':
    routes=[
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph=Graphs(routes)
    start="Mumbai"
    end="New York"
    print(f"betweeen {start} and {end}",route_graph.shortest_path(start,end))