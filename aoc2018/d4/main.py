from collections import namedtuple, Counter
from operator import attrgetter, itemgetter

from aocframework import AoCFramework
import re

Entry = namedtuple('Entry',
                   ['year', 'month', 'day', 'hour', 'minute', 'wakes', 'sleeps', 'guard_id'])


class Day(AoCFramework):
    test_cases = (
        ('''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up''', 240
         ),)

    def parse(self, s):
        pattern = r'\[(?P<year>\d{4})-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] (?P<wakes>wakes up)?(?P<sleeps>falls asleep)?(Guard #(?P<guard_id>\d+) begins shift)?'
        match = re.match(pattern, s)
        data = match.groupdict()
        data['year'] = int(data['year'])
        data['month'] = int(data['month'])
        data['day'] = int(data['day'])
        data['hour'] = int(data['hour'])
        data['minute'] = int(data['minute'])
        data['guard_id'] = data['guard_id'] and int(data['guard_id'])
        data['wakes'] = bool(data['wakes'])
        data['sleeps'] = bool(data['sleeps'])
        entry = Entry(**data)
        return entry

    def go(self):
        parsed = [self.parse(s) for s in self.linesplitted]
        sorted_log = sorted(parsed, key=lambda x: (x.year, x.month, x.day, x.hour, x.minute))
        guard_list = tuple((set(map(attrgetter('guard_id'), sorted_log))) - {None})
        guards = {guard: 0 for guard in guard_list}
        sleeping_minutes = {guard: [] for guard in guard_list}
        current_guard = None
        sleeps_since = None
        for entry in sorted_log:
            if entry.guard_id:
                current_guard = entry.guard_id
            elif entry.sleeps:
                sleeps_since = entry.minute
            elif entry.wakes:
                guards[current_guard] += (entry.minute - sleeps_since)
                sleeping_minutes[current_guard] += list(range(sleeps_since, entry.minute))
                sleeps_since = None

        winner_guard = max(guards.items(), key=itemgetter(1))
        winner_guard_id = winner_guard[0]
        counts = Counter(sleeping_minutes[winner_guard_id]).most_common(1)
        return winner_guard_id * counts[0][0]

Day()
