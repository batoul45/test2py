import pickle

class Bus:
    def __init__(self, route_number, start_point, destination, travel_time):
        # Initialize the Bus class with essential details for each bus.
        # Each bus will have:
        # - route_number: a unique identifier for the route (integer)
        # - start_point: the starting location of the bus (string)
        # - destination: the endpoint of the bus journey (string)
        # - travel_time: the travel duration from start to destination (string)
        self.route_number = route_number
        self.start_point = start_point
        self.destination = destination
        self.travel_time = travel_time

    def get_info(self):
        # Returns a string representing the bus information.
        # The output includes the route number, start point, destination, and travel time.
        return f"Route number: {self.route_number} Starting point: {self.start_point} Destination point: {self.destination} Travel time: {self.travel_time}"

class Autopark:
    def __init__(self):
        # Initialize the Autopark class with an empty list to store multiple Bus objects.
        # This list will store all buses added to the autopark.
        self.buses = []

    def create_autopark(self, n):
        # Create 'n' Bus objects by collecting details from the user.
        # For each bus, ask the user to input the route number, starting point, destination, and travel time.
        # Each Bus object is then added to the 'self.buses' list and saved to a file for future use.
        for i in range(n):
            route_number = int(input(f"Enter the route number of {i + 1} bus: "))
            start_point = input(f"Enter the starting point of {i + 1} bus: ")
            destination = input(f"Enter the destination point of {i + 1} bus: ")
            travel_time = input(f"Enter the travel time of {i + 1} bus: ")
            bus = Bus(route_number, start_point, destination, travel_time)
            self.buses.append(bus)
        # Save the complete list of buses to a file using the 'save_to_file' method.
        self.save_to_file("autopark.pkl")

    def save_to_file(self, filename):
        # Save the list of Bus objects to a file named 'filename'.
        # The 'pickle' module serializes the 'self.buses' list, making it easy to store and retrieve later.
        # 'wb' mode means write-binary mode, as required for pickle.
        with open(filename, "wb") as file:
            pickle.dump(self.buses, file)

    def load_from_file(self, filename):
        # Load the list of Bus objects from a file named 'filename'.
        # Opens the file in 'rb' mode (read-binary) to read the serialized 'self.buses' list.
        # This allows previously saved bus data to be reloaded into the Autopark instance.
        with open(filename, "rb") as file:
            self.buses = pickle.load(file)

    def show_autopark(self):
        # Display information for each bus currently in the autopark.
        # Calls 'get_info()' for each Bus object in 'self.buses' to format and print the details.
        for bus in self.buses:
            print(bus.get_info())

    def sort_by_number(self):
        # Sorts the buses in 'self.buses' in descending order based on the route number.
        # 'key=lambda bus: bus.route_number' extracts the route number from each Bus object.
        # 'reverse=True' sorts the list in descending order.
        self.buses.sort(key=lambda bus: bus.route_number, reverse=True)

    def search_by_point(self, point):
        # Finds and displays buses that either start or end at a specific location ('point').
        # For each Bus in 'self.buses', checks if 'start_point' or 'destination' matches 'point'.
        # If a match is found, it prints the bus's details; otherwise, it informs the user that no buses were found.
        found = False
        for bus in self.buses:
            if bus.start_point == point or bus.destination == point:
                print(bus.get_info())
                found = True
        if not found:
            print("No buses found for this point.")

# Example usage:
autopark = Autopark()

# Uncomment the lines below to interact with the program
# autopark.create_autopark(3)  # Collects input for 3 buses and saves them to a file.
# autopark.load_from_file("autopark.pkl")  # Loads the list of buses from a file.

print("\n>>> show_autopark()")
autopark.show_autopark()  # Display all buses currently in the autopark.

print("\n>>> sort_by_number()")
autopark.sort_by_number()
autopark.show_autopark()  # Display buses sorted by route number in descending order.

print("\n>>> search_by_point('Prague')")
autopark.search_by_point('Prague')  # Search for buses that start or end at 'Prague'.
