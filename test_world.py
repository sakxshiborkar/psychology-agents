from world import World


world = World()

world.add_event("Mara entered the café.")
world.add_event("Daniel left the café.")
world.add_event("The café lights went out.")

world.show_history()
