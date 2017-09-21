from nodes import set_current_node

def send_msg(channel, msg):
    print("TECHIO> message --channel '"+str(channel)+"' '"+str(msg)+"'")

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def test_set_current_node():
    try:
        inf = 999999
        count = set_current_node({"A"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5})
        assert count == "F", 'Running set_current_node({"A"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5}), expected "F", got "' + str(count) + '.'
        count = set_current_node({"A","F"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5})
        assert count == "E", 'Running set_current_node({"A","F"}, {"A":0, "B":5, "C":inf, "D":inf, "E":4, "F":3, "G":5}), expected "E", got "' + str(count) + '.'
        success()

        send_msg("Good job!","Correct. When setting a new current node, you need to pick the non-visited node with the smallest distance.")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Check the solved example again, and step 2 in the algorithm.")

if __name__ == "__main__":
    test_set_current_node()
