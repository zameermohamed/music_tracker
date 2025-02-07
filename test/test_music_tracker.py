from lib.music_tracker import MusicTracker
import pytest
"""
Given a music tracker object is intialised, nothing added, lists tracks returns empty list
"""
def test_returns_empty_list_when_initialised():
	music_tracker = MusicTracker()
	assert music_tracker.list_tracks() == []


"""
Given a single track is added, list track should return a list with that track
"""
def test_returns_list_when_one_track_is_added():
	music_tracker = MusicTracker()
	music_tracker.add_track('sprinter')
	assert music_tracker.list_tracks() == ['sprinter']


"""
Given two tracks are added, list track should return a list with that track
"""
def test_multiple_tracks_added():
	music_tracker = MusicTracker()
	music_tracker.add_track('sprinter')
	music_tracker.add_track('baby shark')
	assert music_tracker.list_tracks() == ['sprinter', 'baby shark']

"""
Given an empty string - raise exception
"""
def test_raise_exception_when_empty_string_added():
	music_tracker = MusicTracker()

	with pytest.raises(Exception) as e:
		music_tracker.add_track('') # raises exception

	err_msg = str(e.value)
	assert err_msg == "Input value was an empty string!"


"""
Given an non string type - raise exception
"""
def test_raise_exception_when_empty_string_added():
	music_tracker = MusicTracker()

	with pytest.raises(Exception) as e:
		music_tracker.add_track(123) # raises exception

	err_msg = str(e.value)
	assert err_msg == "Input value was not a string!"
