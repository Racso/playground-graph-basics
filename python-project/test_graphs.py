from graphs import get_graph_info

def send_msg(channel, msg):
    print("TECHIO> message --channel '"+str(channel)+"' '"+str(msg)+"'")

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def test_get_graph_info():
    try:
        graph = [[1,3],[1,4],[4,5],[1,3],[3,2],[5,2],[5,5],[3,4]]
        a,b,c = get_graph_info(graph)
        assert a==4 and b==1 and c==True, "Failed on test #1."

        graph = [[1,2],[3,1],[2,1],[3,2]]
        a,b,c = get_graph_info(graph)
        assert a==3 and b==0 and c==True, "Failed on test #2."

        graph = [[1,1],[2,2],[3,3],[3,3]]
        a,b,c = get_graph_info(graph)
        assert a==4 and b==3 and c==True, "Failed on test #3."

        graph = [[1,2],[1,3],[1,4],[2,4],[3,4],[4,4]]
        a,b,c = get_graph_info(graph)
        assert a==5 and b==1 and c==False, "Failed on test #4."

        success()

        send_msg("Good job!","Correct!")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "A loop is an edge that connects a node with itself, and adds 2 to the degree of the node.")
        send_msg("Hint 💡", "The graph is undirected, so an edge from A to B and an edge from B to A are parallel.")

if __name__ == "__main__":
    test_get_graph_info()
