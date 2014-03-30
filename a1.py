def seconds_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    '''

    return time_2 - time_1


def hours_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    '''

    return time_2/3600 - time_1/3600



def to_float_hours(hours, minutes, seconds):
   '''(int, int, int) -> float

   Return the total number of hours in the specified number
   of hours, minutes, and seconds.
   
   Precondition: 0 <= minutes < 60  and  0 <= seconds < 60
   
   >>> to_float_hours(0, 15, 0)
   0.25
   >>> to_float_hours(2, 45, 9)
   2.7525
   >>> to_float_hours(1, 0, 36)
   1.01
   '''
   return hours + minutes/60 + seconds/3600


def to_24_hour_clock(hours):
    '''(number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    '''

    return hours % 24



### Write your get_hours function definition here:

def get_hours(sec):
    '''(int) -> int

    Return hours component of time in sec seconds
    when converted to hours:minutes:seconds format.

    >>> get_hours(3800)
    1
    >>> get_hours(400)
    0
    >>> get_hours(93960)
    2
    '''

    return to_24_hour_clock(sec // 3600)

### Write your get_minutes function definition here:

def get_minutes(sec):
    '''(int) -> int

    Return minutes component of time in sec seconds
    when converted to hours:minutes:seconds format.

    >>> get_minutes(3800)
    3
    >>> get_minutes(400)
    6
    >>> get_minutes(93960)
    6
    '''
    
    return (sec % 3600) // 60

### Write your get_seconds function definition here:

def get_seconds(sec):
    '''(int) -> int

    Return seconds component of time in sec seconds
    when converted to hours:minutes:seconds format.

    >>> get_seconds(3800)
    20
    >>> get_seconds(400)
    40
    >>> get_seconds(93960)
    0
    '''

    return (sec % 60)

def time_to_utc(utc_offset, time):
    '''(number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+1, 12.2)
    11.2
    >>> time_to_utc(-1, 12.1)
    13.0
    >>> time_to_utc(-1, 23.0)
    0.0
    '''
    return to_24_hour_clock(time - utc_offset)


def time_from_utc(utc_offset, time):
    '''(number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+1, 12.2)
    13.2
    >>> time_from_utc(-1, 12.1)
    11.1
    >>> time_from_utc(-1, 23.0)
    22.0
    '''

    return to_24_hour_clock(time + utc_offset)

