import json

class TrainSimulation:
    """
    Manages the state and simulation logic for the train network.
    """
    def __init__(self, trains_file='trains.json', sections_file='sections.json'):
        self.trains = {}
        self.sections = {}
        self.disruptions = {}
        self.load_data(trains_file, sections_file)

    def load_data(self, trains_file, sections_file):
        """Loads train and section data from JSON files."""
        try:
            with open(trains_file, 'r') as f:
                trains_list = json.load(f)
                self.trains = {train['train_id']: train for train in trains_list}

            with open(sections_file, 'r') as f:
                sections_list = json.load(f)
                self.sections = {section['section_id']: section for section in sections_list}
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error loading data: {e}. Please ensure the files exist.")
            self.trains = {}
            self.sections = {}

    def _convert_time_to_minutes(self, time_str):
        """Helper to convert "HH:MM" time string to total minutes from midnight."""
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    def _convert_minutes_to_time(self, total_minutes):
        """Helper to convert total minutes from midnight back to "HH:MM" string."""
        h = int(total_minutes / 60)
        m = int(total_minutes % 60)
        return f"{h:02d}:{m:02d}"

    def delay_train(self, train_id, minutes):
        """
        Applies a delay to a train's entire schedule.

        Args:
            train_id (str): The ID of the train to delay.
            minutes (int): The number of minutes to add to the schedule.
        """
        if train_id not in self.trains:
            print(f"Error: Train {train_id} not found.")
            return

        print(f"Delaying train {train_id} by {minutes} minutes...")
        train = self.trains[train_id]
        
        for stop in train['schedule']:
            arrival_minutes = self._convert_time_to_minutes(stop['arrival_time'])
            departure_minutes = self._convert_time_to_minutes(stop['departure_time'])

            stop['arrival_time'] = self._convert_minutes_to_time(arrival_minutes + minutes)
            stop['departure_time'] = self._convert_minutes_to_time(departure_minutes + minutes)
        
        print(f"Train {train_id} schedule updated.")

    def block_section(self, section_id, duration_minutes):
        """
        Simulates a blockage on a specific section of track.

        This adds a new disruption to the simulation state.
        Args:
            section_id (str): The ID of the section to block.
            duration_minutes (int): The duration of the blockage in minutes.
        """
        if section_id not in self.sections:
            print(f"Error: Section {section_id} not found.")
            return
        
        print(f"Blocking section {section_id} for {duration_minutes} minutes.")
        # In a real simulation, you would use a time component to track
        # when the block starts and ends. For simplicity, we'll just store it.
        self.disruptions[section_id] = {
            'type': 'blockage',
            'duration': duration_minutes
        }

    def reroute_train(self, train_id, new_path):
        """
        Reroutes a train to a new schedule path.

        Args:
            train_id (str): The ID of the train to reroute.
            new_path (list): A new list of dictionaries representing the new schedule.
        """
        if train_id not in self.trains:
            print(f"Error: Train {train_id} not found.")
            return

        print(f"Rerouting train {train_id} to a new path.")
        self.trains[train_id]['schedule'] = new_path

    def run_simulation(self):
        """
        A placeholder for a full simulation loop.
        In a real scenario, this would iterate through time and process events.
        """
        print("\n--- Running Simulation ---")
        # Example of applying a delay from a loaded disruption scenario
        if 'T-001' in self.trains:
             self.delay_train('T-001', 30) # Example manual delay
        
        print("\n--- Simulation Complete ---")
        self.print_current_state()

    def print_current_state(self):
        """Prints the current state of trains and disruptions."""
        print("\nCurrent Train Schedules:")
        print(json.dumps(self.trains, indent=4))
        print("\nCurrent Disruptions:")
        print(json.dumps(self.disruptions, indent=4))

# Example usage
if __name__ == '__main__':
    sim = TrainSimulation()
    sim.run_simulation()