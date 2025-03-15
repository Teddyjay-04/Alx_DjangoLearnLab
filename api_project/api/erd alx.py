from graphviz import Digraph

# Create a new directed graph
dot = Digraph(format="png")

# Define the entities (tables)
dot.node("Book", "Book\n- id\n- title\n- author_id\n- publication_year\n- ISBN")
dot.node("Author", "Author\n- id\n- name\n- date_of_birth\n- biography")
dot.node("User", "User\n- id\n- username\n- email\n- profile_photo\n- date_of_birth\n- password")

# Define relationships (edges)
dot.edge("Author", "Book", label="1 to Many")
dot.edge("User", "Book", label="1 to Many")

# Render and save the ERD
dot.render("erd_diagram")

print("ERD saved as erd_diagram.png")
