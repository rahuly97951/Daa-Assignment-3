def find_content_children(g, s):
    
    g.sort()
    s.sort()

    child_i = 0  
    cookie_i = 0  
    
    
    while child_i < len(g) and cookie_i < len(s):
        if s[cookie_i] >= g[child_i]:
           
            child_i += 1  
        cookie_i += 1

    return child_i  

# Example usage
if __name__ == "__main__":
    g = [1, 2, 3]  # Greed factor of children
    s = [1, 1]     # Sizes of cookies

    result = find_content_children(g, s)
    print("Maximum number of content children =", result)
