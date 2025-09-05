import json

def convert_time_to_minutes(time_str):
    """
    Converts a time string in "HH:MM" format to minutes from midnight.
    e.g., "08:30" -> 510
    """
    try:
        h, m = map(int, time_str.split(':'))
        return h * 60 + m
    except ValueError:
        return None

def validate_data(trains_file='trains.json', sections_file='sections.json'):
    """
    Performs comprehensive validation on the train and section data.
    """
    try:
        with open(trains_file, 'r') as f:
            trains_data = json.load(f)
        
        with open(sections_file, 'r') as f:
            sections_data = json.load(f)

        print("Starting data validation...")
        
        # Validate each train
        for train in trains_data:
            if not all(k in train for k in ["train_id", "type", "priority", "schedule"]):
                print(f"Validation Error: Train {train.get('train_id', 'N/A')} is missing required fields.")
                continue

            # Validate timing consistency
            if not validate_timing_consistency(train):
                print(f"Validation Error: Timing inconsistency in train {train['train_id']}.")

        # Validate for section conflicts (conceptual check)
        # This is a complex check that requires a time-based simulation,
        # so this function provides a conceptual overview.
        if not validate_section_conflicts(trains_data, sections_data):
             print("Validation Warning: Potential section conflicts detected.")
        else:
             print("Section conflict validation passed.")

        print("Data validation complete.")
        return True

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure trains.json and sections.json exist.")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in data files: {e}.")
        return False

def validate_timing_consistency(train):
    """
    Checks if departure times are after arrival times for a given train.
    """
    for stop in train['schedule']:
        if not all(k in stop for k in ["station", "arrival_time", "departure_time"]):
            print(f"  - Missing fields in stop: {stop}")
            return False

        arrival_minutes = convert_time_to_minutes(stop['arrival_time'])
        departure_minutes = convert_time_to_minutes(stop['departure_time'])

        if arrival_minutes is None or departure_minutes is None:
            print(f"  - Invalid time format in schedule for {train['train_id']}.")
            return False
            
        if departure_minutes < arrival_minutes:
            print(f"  - Departure time for {stop['station']} is before arrival time.")
            return False
    return True

def validate_section_conflicts(trains_data, sections_data):
    """
    Checks for potential conflicts where two trains might be in the same
    single-track section at the same time.

    This is a high-level conceptual check. A full implementation would
    require a detailed simulation of train movement.
    """
    # A dictionary to map station pairs to section IDs for easier lookup.
    section_map = {(s['from_station'], s['to_station']): s['section_id'] for s in sections_data}

    # Iterate through each pair of trains to check for schedule overlaps.
    for i, train1 in enumerate(trains_data):
        for j, train2 in enumerate(trains_data):
            if i >= j:  # Avoid checking the same pair twice
                continue

            # This is a simplified check. A more robust solution would track
            # train location and time on each section of track.
            # Example check: look for two trains scheduled to depart the same station at similar times,
            # especially if the next section is single-track.
            for s1_index in range(len(train1['schedule']) - 1):
                stop1_depart = convert_time_to_minutes(train1['schedule'][s1_index]['departure_time'])
                stop1_arrival_next = convert_time_to_minutes(train1['schedule'][s1_index+1]['arrival_time'])

                for s2_index in range(len(train2['schedule']) - 1):
                    stop2_depart = convert_time_to_minutes(train2['schedule'][s2_index]['departure_time'])
                    stop2_arrival_next = convert_time_to_minutes(train2['schedule'][s2_index+1]['arrival_time'])

                    # Check for time overlap
                    time_overlap = max(stop1_depart, stop2_depart) < min(stop1_arrival_next, stop2_arrival_next)

                    # Check for section conflict
                    section_from1 = train1['schedule'][s1_index]['station']
                    section_to1 = train1['schedule'][s1_index+1]['station']
                    section_from2 = train2['schedule'][s2_index]['station']
                    section_to2 = train2['schedule'][s2_index+1]['station']

                    section1_id = section_map.get((section_from1, section_to1))
                    section2_id = section_map.get((section_from2, section_to2))

                    if section1_id == section2_id and section1_id is not None and sections_data[int(section1_id[2:])-1]['capacity_tracks'] == 1 and time_overlap:
                        print(f"  - Conflict detected on single-track section {section1_id} between trains {train1['train_id']} and {train2['train_id']}.")
                        return False
    return True

# Example usage
if __name__ == '__main__':
    validate_data()
