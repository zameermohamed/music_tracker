# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:None   
        # Side effects:
        #   creates epmty list to track music
        pass # No code here yet

    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the list with track
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   As a list of strings
        #   if nothing exists return empty list
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a music tracker object is intialised, nothing added, lists tracks returns empty list
"""
music_tracker = MusicTracker()
assert music_tracker.list_tracks() == []


"""
Given a single track is added, list track should return a list with that track
"""
music_tracker = MusicTracker()
music_tracker.add_track('sprinter')
assert music_tracker.list_tracks() == ['sprinter']


"""
Given two tracks are added, list track should return a list with that track
"""
music_tracker = MusicTracker()
music_tracker.add_track('sprinter')
music_tracker.add_track('baby shark')
assert music_tracker.list_tracks() == ['sprinter', 'baby shark']

"""
Given an empty string - raise exception
"""
music_tracker = MusicTracker()
music_tracker.add_track('') # raises exception


"""
Given an non string type - raise exception
"""
music_tracker = MusicTracker()
music_tracker.add_track(123) # raises exception


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
