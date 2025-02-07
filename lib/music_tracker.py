class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:None   
        # Side effects:
        #   creates epmty list to track music
        self.track_list = []

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the list with track
        if not isinstance(track, str):
            raise Exception("Input value was not a string!")
        if track == "":
            raise Exception("Input value was an empty string!")
        self.track_list.append(track)

    def list_tracks(self):
        # Returns:
        #   As a list of strings
        #   if nothing exists return empty list
        # Side-effects:
        #   None
        return self.track_list